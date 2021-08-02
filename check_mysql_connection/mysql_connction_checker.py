#! /usr/bin/python3

# env variable has been set by 'export' commnad
# export DWS_MYSQL_DATABASE_URI=localhost

from os import environ, getenv
from sys import stderr, stdout
from mysql import connector
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

def check_connection(): 
    try:

        url = environ.get('DWS_MYSQL_DATABASE_URI')
        dbc = urlparse(url)
        host = dbc.hostname
        user = dbc.username
        scheme = dbc.scheme
        password = dbc.password
        path = dbc.path.lstrip('/')
        print(f'host: {host}, user: {user}, password: {password}, scheme: {scheme}, path: {path}')

        mydb = connector.connect(
            host= host,
            user= user,
            passwd= password
        )

        if (mydb.is_connected()) :
            return 0; 
        else: 
            return 1; 
    
    except Exception as e: 
        print(e)
        print('error in connecting!')
        return 1


if __name__ == "__main__" : 
    
    connection_result = check_connection()

    if( connection_result == 0) : 
        stdout.write('connection performed successfully')
    else: 
        stderr.write('connection failed')
