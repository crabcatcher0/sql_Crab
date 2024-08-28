"""
    : Datatypes
"""
import sqlite3
from .settings import DATABASE_NAME


class DataTypes:
    
    @staticmethod
    def varchar(max_length=255, unique=False):
        unique_const = "UNIQUE" if unique else ""
        return f'VARCHAR({max_length}) NOT NULL {unique_const}'.strip()



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
    

    @staticmethod
    def datetimefield(auto_add_now=True):
        if auto_add_now:
            return  'DATETIME DEFAULT CURRENT_TIMESTAMP'
        
    
    @staticmethod
    def foreignkey(field_name: str, model: str):
        return f"{field_name} INTEGER, FOREIGN KEY ({field_name}) REFERENCES {model}(id)"
        


        



