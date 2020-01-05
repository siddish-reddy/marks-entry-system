import pyodbc
import os
import sys
from datetime import datetime
from config import DB_FILE, PWD, DEBUG


def getTimestamp():
    return datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%M")


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

        con_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='\
                    + resource_path(DB_FILE) \
                    + f';PWD={PWD};'
        self.__connection = pyodbc.connect(con_str)

        self.table = table
        if not self.__table_in_db(table):

            command = f' CREATE TABLE {table} ' + \
                        '(SubjectCode CHAR, ' + \
                        'SubjectTitle CHAR, ' + \
                        'ScriptNo INTEGER, ' + \
                        'Entry SMALLINT,' + \
                        'DataOperatorName CHAR,' + \
                        'TimeDate CHAR, ' + \
                        'Marks SMALLINT, ' + \
                        'RegistrationNo INTEGER);'
            self.__execute(command)

    def __execute(self, command):
        if DEBUG:
            print(command)

        cursor = self.__connection.cursor()
        cursor.execute(command)
        cursor.commit()
        cursor.close()
        return True

    def __table_in_db(self, table):
        cursor = self.__connection.cursor()
        return cursor.tables(table=table).fetchone()

    def insert(self, subject_code, subject_title,
               script_no, entry, data_operator_name,
               marks=None, registration_no=None):

        if marks and not registration_no:
            command = f"INSERT INTO {self.table} \
                        (SubjectCode, SubjectTitle, ScriptNo, \
                        Entry, DataOperatorName, Marks, TimeDate)\
                        VALUES('{subject_code}','{subject_title}',{script_no},\
                                {entry}, '{data_operator_name}', \
                                {marks},'{getTimestamp()}')"

        elif registration_no and not marks:
            command = f"INSERT INTO {self.table} \
                        (SubjectCode, SubjectTitle, ScriptNo, \
                        Entry, DataOperatorName, RegistrationNo,, TimeDate) \
                        VALUES('{subject_code}','{subject_title}', \
                                {script_no},{entry},'{data_operator_name}', \
                                {registration_no}, '{getTimestamp()}')"

        else:
            return False
        return self.__execute(command)

    def __del__(self):
        self.__connection.commit()
        self.__connection.close()
