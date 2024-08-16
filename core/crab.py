import sqlite3


class Crab:

    def __init__(self, database_name: str):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()


    @classmethod 
    def create_table(cls, database_name: str, table_name: str, columns: dict):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # check if the table already exists
        cursor.execute(f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
        """)
        result = cursor.fetchone()

        if result:
            print(f"Table '{table_name}' already exists.")
        else:
            # create table with columns
            columns_definition = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
            cursor.execute(f"""
                CREATE TABLE {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {columns_definition}
            )
            """)
            print(f"Table '{table_name}' created.")
        conn.commit()
        conn.close()


    @classmethod
    def add_column(cls, database_name: str, table_name: str, column_name: str, data_type):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        try:
            cursor.execute(f"""
                ALTER TABLE {table_name}
                ADD COLUMN {column_name} {data_type}
            """)
            print(f"Colum '{column_name}' created.")

        except Exception as e:
            print("Error:", str(e))    

        conn.commit()
        conn.close()


    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.table_name = cls.__name__.lower() 

        cls.create_table(
            database_name='test.db',
            table_name=cls.table_name,
            columns=cls._columns
        )



class DataTypes:

    @classmethod
    def varchar(cls):
        v = 'VARCHAR(255)'
        return v
    
    @classmethod
    def integer(cls):
        i = 'INTEGER'
        return i
    


