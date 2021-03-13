import os

user = os.environ.get('USERNAME');
pw = os.environ.get('PASSWORD');
oracle_client = '/usr/lib/oracle/21/client64/lib';
connect_string = os.environ.get('CONNECT_STRING') + '?' \
                     'wallet_location=/usr/lib/oracle/21/client64/lib/network/admin&retry_delay=3';