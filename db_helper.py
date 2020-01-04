import pyodbc
import os
import sys
from datetime import datetime

DB_FILE = 'db.accdb'

def getTimestamp():
    # return datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%M")
    return datetime.now()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Database:
    def __init__(self, table):
        self.__connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ='+ resource_path(DB_FILE)+ ';PWD=Admin@SVU2020;')
        self.table = table
        if not self.table_in_db(table):
            command = f'CREATE TABLE {table} (SubjectCode CHAR, SubjectTitle CHAR, ScriptNo INTEGER, Entry SMALLINT,  DataOperatorName CHAR, Marks SMALLINT, RegistrationNo INTEGER);'
            self.__execute(command)

    def __execute(self, command):
        cursor = self.__connection.cursor()
        cursor.execute(command)
        cursor.close()

    def table_in_db(self,table):
        cursor = self.__connection.cursor()
        return cursor.tables(table=table).fetchone()

    def insert(self, **kwargs):
        query = f'INSERT INTO'
        self.__execute()

    def __del__(self):
        self.__connection.commit()
        self.__connection.close()
