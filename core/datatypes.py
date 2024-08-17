from datetime import datetime

class DataTypes:
    
    @classmethod
    def varchar(cls):
        v = 'VARCHAR(255)'
        return v
    
    @classmethod
    def integer(cls):
        i = 'INTEGER'
        return i
    
    @classmethod
    def text(cls):
        t = 'TEXT'
        return t
    
    @classmethod
    def date_time(cls, auto_add_now = None):
        if auto_add_now == True:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            return dt_string

