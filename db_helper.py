import pyodbc
import win32com.client
import os.path
from datetime import datetime
from config import DB_FILE, PWD, DEBUG


def getTimestamp():
    return datetime.now().strftime("%d-%m-%Y-%H-%M-%S")


def db_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """

    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def create_db(db_path):
    if not os.path.isfile(db_path):
        print('creating database')
        # ACE.DAO constants
        dbLangGeneral = ";LANGID=0x0409;CP=1252;COUNTRY=0"
        dbVersion120 = 128
        dbEncrypt = 2
        dbe = win32com.client.Dispatch("DAO.DBEngine.120")
        dbe.CreateDatabase(db_path,
                           dbLangGeneral + ";pwd=" + PWD,
                           dbVersion120 + dbEncrypt)


create_db(db_path(DB_FILE))


class Database:

    """Initiate the class and call insert function.
       db = Database(tableName); # tableName = subjectCode + str(startingNo);
       db.insert(subject_code, subject_title, script_no,
                 entry, data_operator_name, marks|registration_no);
    """

    def __init__(self,
                 subject_code,
                 title, starting_no,
                 no_of_scripts,
                 entry,
                 data_operator_name
                 ):

        con_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='\
                    + db_path(DB_FILE) \
                    + f';PWD={PWD};'
        self.__connection = pyodbc.connect(con_str)

        self.table = subject_code + '_' + str(starting_no)
        self.subject_code = subject_code
        self.title = title
        self.starting_no = starting_no
        self.no_of_scripts = no_of_scripts
        self.entry = entry
        self.data_operator_name = data_operator_name

        if not self.__table_in_db(self.table):

            command = f' CREATE TABLE {self.table} ' + \
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

    def insert(self, script_no,
               marks=None, registration_no=None):

        if marks and not registration_no:
            command = f"INSERT INTO {self.table} \
                        (SubjectCode, SubjectTitle, ScriptNo, \
                        Entry, DataOperatorName, Marks, TimeDate)\
                        VALUES('{self.subject_code}','{self.title}',{script_no},\
                                {self.entry}, '{self.data_operator_name}', \
                                {marks},'{getTimestamp()}')"

        elif registration_no and not marks:
            command = f"INSERT INTO {self.table} \
                        (SubjectCode, SubjectTitle, ScriptNo, \
                        Entry, DataOperatorName, RegistrationNo, TimeDate) \
                        VALUES('{self.subject_code}','{self.title}',{script_no},\
                                {self.entry},'{self.data_operator_name}', \
                                {registration_no}, '{getTimestamp()}')"

        else:
            return False
        return self.__execute(command)

    def __del__(self):
        self.__connection.commit()
        self.__connection.close()
