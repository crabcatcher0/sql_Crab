from crab.core.mysql_orm.mysql_settings import MySQLConnection
from database import DATABASE_NAME, HOST, PASSWORD, PORT, USER
import mysql

start = MySQLConnection(database=DATABASE_NAME, host=HOST, password=PASSWORD, port=PORT, user=USER)


class CrabMysql:

    @classmethod
    def create(cls, model: str, fields: dict):
        col_dtype = ", ".join([f"{col} {dtype}" for col, dtype in fields.items()])
        query = f"""
            CREATE TABLE {model} 
            ({model}_id INTEGER AUTO_INCREMENT PRIMARY KEY,
            {col_dtype});
            """
        start.execute_query(query=query)
        start.close()

    
    @classmethod
    def new_field(cls, model: str, field: str, datatype):
        try:
            query = f"""
                ALTER TABle {model}
                ADD COLUMN {field} {datatype};
            """
            start.execute_query(query=query)

        except Exception as e:
            print(f"Error in fields: {str(e)}.")

        finally:
            start.close()




    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        model = cls.__name__.lower()

        fields = {
            attr: value for attr, value in cls.__dict__.items() if not callable(value)
            and not attr.startswith("__")
        }
        
        cls.create(
            model=model,
            fields=fields
        )


    @staticmethod
    def charField(max_length=255):
        return f"CHAR({max_length})"

    @staticmethod
    def intField():
        return "INTEGER"
