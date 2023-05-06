import pyodbc
import os
import urllib
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database info
server = os.getenv("SERVER_URI")
database = os.getenv("DATABASE_NAME")
username = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
driver = pyodbc.drivers()[-1]

# define the connection string to the SQL Server
connection_string = f'Driver={driver};Server=tcp:{server},1433;Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
connection_string = connection_string.replace('\r', '').replace('\n', '') # for some reason some special charactors are added and causes errors without this line of code.


# connctor engine 
odbc_connect = urllib.parse.quote_plus(connection_string)
engine = create_engine('mssql+pyodbc:///?odbc_connect=' + odbc_connect)

# create session which will be used in crud.py
SessionLocal = sessionmaker(bind=engine)

# Base class which will be used in model.py
Base = declarative_base()


if __name__ == '__main__':
    # connection test
    with engine.connect() as conn:
        rs = conn.execute(text('SELECT @@VERSION as version'))
        for row in rs:
            print(row)