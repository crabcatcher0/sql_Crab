import sqlite3
from settings import DATABASE_NAME



class CrabModel:

    @classmethod
    def table(cls, table_name: str, column: dict):
        database_name = DATABASE_NAME
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
        """)

        result = cursor.fetchone()
        if result:
            print(f"Table '{table_name}' already exists. Skipping...")
        else:
            colmn_def = ", ".join([f"{col} {dtype}" for col, dtype in column.items()])
            try:
                cursor.execute(f"""
                    CREATE TABLE {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {colmn_def}
                    );
                """)
                print(f"Table '{table_name}' created.\nColumn: {', '.join(column.keys())} created.")
            except (sqlite3.OperationalError, Exception) as e:
                print(f'Error: {str(e)}')

        conn.commit()
        conn.close()


    @classmethod
    def add_column(cls, table_name: str, column_name: str, data_type: str):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
                ALTER TABLE {table_name}
                ADD COLUMN {column_name} {data_type};
        """)
            print(f"Column '{column_name}' created.")
        except Exception as e:
            print(f'Error: {str(e)}')

        conn.commit()
        conn.close()



    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.table_name = cls.__name__.lower()
        cls.model = cls.__name__.lower()

        cls.table(
            table_name = cls.table_name,
            column = cls._column
        )

       
@staticmethod
def foreignkey(model: str, col_name: str, ref_model, ref_col):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(f"""
            ALTER TABLE {model}
            ADD CONSTRAINT fk_{col_name} 
            FOREIGN KEY ({col_name}) 
            REFERENCES {ref_model} ({ref_col});
        """)
        print('Foreign Key Added...Ok..')
    except Exception as e:
        print(f'Error: {str(e)}')
        
        conn.commit()
        conn.close()



