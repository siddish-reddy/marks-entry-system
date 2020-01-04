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

    base_path = getattr(sys,
                        '_MEIPASS',
                        os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(base_path, relative_path)


class Database:

    """Initiate the class and call insert function.
       db = Database(tableName);
       db.insert(subject_code, subject_title, script_no,
                 entry, data_operator_name, marks|registration_no);
    """

    def __init__(self, table):
        self.__connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};\
                                            DBQ=' + resource_path(DB_FILE)
                                           + ';PWD=Admin@SVU2020;')
        self.table = table
        if not self.table_in_db(table):
            command = f'CREATE TABLE {table} \
                (SubjectCode CHAR,\
                 SubjectTitle CHAR, \
                 ScriptNo INTEGER, \
                 Entry SMALLINT, \
                 DataOperatorName CHAR, \
                 Marks SMALLINT, \
                 RegistrationNo INTEGER);'

            self.__execute(command)

    def __execute(self, command):
        cursor = self.__connection.cursor()
        cursor.execute(command)
        cursor.close()
        return True

    def table_in_db(self, table):
        cursor = self.__connection.cursor()
        return cursor.tables(table=table).fetchone()

    def insert(self, subject_code, subject_title,
               script_no, entry, data_operator_name,
               marks=None, registration_no=None):

        if marks and not registration_no:
            command = f'INSERT INTO {self.table} \
                    (SubjectCode, SubjectTitle, ScriptNo,\
                     Entry, DataOperatorName, Marks)\
                    VALUES({subject_code} {subject_title} {script_no}\
                           {entry} {data_operator_name} {marks})'

        elif registration_no and not marks:
            command = f'INSERT INTO {self.table} \
                    (SubjectCode, SubjectTitle, ScriptNo,\
                     Entry, DataOperatorName, RegistrationNo)\
                    VALUES({subject_code} {subject_title} {script_no}\
                           {entry} {data_operator_name} {registration_no})'

        else:
            return False

        return self.__execute(command)

    def __del__(self):
        self.__connection.commit()
        self.__connection.close()
