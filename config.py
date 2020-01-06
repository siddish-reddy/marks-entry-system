DEBUG = True
DB_FILE = 'marks_db.accdb'

try:
    from secrets import PWD
except ImportError:
    PWD = 'dummy'
