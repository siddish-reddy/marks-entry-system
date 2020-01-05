DEBUG = False
DB_FILE = 'db.accdb'

try:
    from secrets import PWD
except ImportError:
    PWD = 'dummy'
