import sqlite3
from .settings import DATABASE_NAME


class DataTypes:
    
    @staticmethod
    def varchar(max_length=255):
        return f'VARCHAR({max_length}) NOT NULL'


    @staticmethod
    def integer():
        return 'INTEGER NOT NULL'


    @staticmethod
    def boolean():
        return 'BOOLEAN'


    @staticmethod
    def emailfield(unique = True):
        if unique:
            return 'VARCHAR(255) UNIQUE NOT NULL'
        else:
            return 'VARCHAR(255) UNIQUE NOT NULL'
        



