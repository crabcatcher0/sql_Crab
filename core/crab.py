import sqlite3


class Crab:

    def __init__(self, database_name: str):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()


    @classmethod 
    def create_table(cls, database_name: str, table_name: str):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        #first check
        cursor.execute(f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';""") 
        result = cursor.fetchone()

        if result:
            print(f"Table '{table_name}' already exists.")
        else:
            cursor.execute(f"""
            CREATE TABLE {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT
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
    def varchar(cls):
        v = 'VARCHAR(255)'
        return v
    
    @classmethod
    def integer(cls):
        i = 'INTEGER'
        return i
    


class Student(Crab):
    database = 'test.db'
    table_name = 'students'
    table = Crab.create_table(database, 'students')
    name = Crab.add_column(database, table_name, 'name', data_type=Crab.varchar())
    subject = Crab.add_column(database, table_name, 'subject', data_type=Crab.varchar())
    age = Crab.add_column(database, table_name, 'age', Crab.varchar())

    