# Based on: https://blogs.oracle.com/opal/how-to-use-python-flask-with-oracle-database

import cx_Oracle
from invoiceservice.app.api import db_config

pool = None

def init_db():
    cx_Oracle.init_oracle_client(lib_dir=db_config.oracle_client)

def init_session(connection, requestedTag_ignored):
    cursor = connection.cursor()
    cursor.execute("""
        ALTER SESSION SET
          TIME_ZONE = 'UTC'
          NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI'""")

def start_pool():

    # Generally a fixed-size pool is recommended, i.e. pool_min=pool_max.
    # Here the pool contains 4 connections, which is fine for 4 conncurrent
    # users.
    #
    # The "get mode" is chosen so that if all connections are already in use, any
    # subsequent acquire() will wait for one to become available.
    #
    # Note there is no explicit 'close cursor' or 'close connection'.  At the
    # end-of-scope when init_session() finishes, the cursor and connection will be
    # closed automatically.  In real apps with a bigger code base, you will want to
    # close each connection as early as possible so another web request can use it.

    pool_min = 4
    pool_max = 4
    pool_inc = 0
    pool_gmd = cx_Oracle.SPOOL_ATTRVAL_WAIT

    username = db_config.user
    password = db_config.pw
    connect_string = db_config.connect_string

    print("Connecting to", connect_string)

    global pool
    pool = cx_Oracle.SessionPool(user=username,
                                 password=password,
                                 dsn=connect_string,
                                 min=pool_min,
                                 max=pool_max,
                                 increment=pool_inc,
                                 threaded=True,
                                 getmode=pool_gmd,
                                 sessionCallback=init_session)

def fetch_all_invoices():
    connection = pool.acquire()
    cursor = connection.cursor()
    sql = "select to_char(invoice_date, 'yyyy-mm-dd') as invoice_date, invoice_number, total from invoices where " \
          "total > :total_var order by total"
    total_var = 200
    cursor.execute(sql, [total_var])

    cursor.rowfactory = lambda *args: dict(zip([d[0] for d in cursor.description], args))
    data = cursor.fetchall()

    return data