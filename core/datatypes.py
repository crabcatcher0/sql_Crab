
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
    