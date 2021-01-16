import cx_Oracle
import db_config

def connect_db():
    cx_Oracle.init_oracle_client(lib_dir="/Users/andrejb/mywork/cloud/db/instantclient_19_8")

    username = db_config.user
    password = db_config.pw
    connect_string = "tcps://adb.eu-frankfurt-1.oraclecloud.com:1522/n3irgbwjvjxwqfk_katanadb_medium.adb.oraclecloud.com?" \
                     "wallet_location=/Users/andrejb/infra/shared/wallets/Wallet_katanaDB&retry_delay=3"

    connection = cx_Oracle.connect(username, password, connect_string)

    cursor = connection.cursor()

    sql = "select TO_CHAR(INVOICE_DATE, 'YYYY-MM-DD') AS INVOICE_DATE, INVOICE_NUMBER, TOTAL from invoices where " \
          "total > :total_var order by total"

    print("Fetch each row as a Dictionary")
    cursor.execute(sql, total_var=200)
    columns = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args: dict(zip(columns, args))
    for row in cursor:
        print(row)

if __name__ == '__main__':
    connect_db()
