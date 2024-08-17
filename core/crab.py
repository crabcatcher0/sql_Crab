import sqlite3
from settings import DATABASE_NAME

class Crab:

    @classmethod
    def create_table(cls, database_name: str, table_name: str, columns: dict):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
        """)
        result = cursor.fetchone()

        if result:
            print(f"Table '{table_name}' already exists. Skipping...")
            
            # add column if they don't exist
            for col, dtype in columns.items():
                try:
                    cursor.execute(f"""
                        ALTER TABLE {table_name}
                        ADD COLUMN {col} {dtype}
                    """)
                    print(f"Column '{col}' added to table '{table_name}'. Success...")

                except sqlite3.OperationalError as e:
                    if "duplicate column name" in str(e).lower():
                        print(f"Column '{col}' already exists in '{table_name}'. Skipping...")
                    else:
                        raise e
        else:
            
            columns_def = ""

            for col, dtype in columns.items():
                columns_def += f"{col} {dtype}, "

            columns_def = columns_def.rstrip(", ")

            cursor.execute(f"""
                CREATE TABLE {table_name}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {columns_def}
                )""")
            print(f"Table '{table_name}' created. Success...")

        conn.commit()
        conn.close()


    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.table_name = cls.__name__.lower()

        cls.create_table(
            database_name=DATABASE_NAME,
            table_name=cls.table_name,
            columns=cls.columns
        )


    @classmethod
    def add_data(cls, table_name: str, columns: tuple, values: tuple):
        database_name = DATABASE_NAME
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
    
        cursor.execute(f"""
                INSERT INTO {table_name} {columns}
                VALUES {values};
        """)
        print('Data Added...')
        
        conn.commit()
        conn.close()




