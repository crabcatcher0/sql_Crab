import sqlite3
from .settings import DATABASE_NAME


class Data:

    @classmethod
    def add_data(cls, table_name: str, column: dict):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        columns = ', '.join(column.keys())
        placeholders = ', '.join(['?' for _ in column.values()])
        values = tuple(column.values())
        try:
            cursor.execute(f"""
                INSERT INTO {table_name} ({columns}) VALUES ({placeholders})
            """, values)

            print(f'Data added to {table_name}....')
            
        except Exception as e:
            print(f'Error: {str(e)}')

        conn.commit()
        conn.close()


    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls.table_name = cls.__name__.lower()

        cls.add_data(
            table_name=cls.table_name,
            column=cls._data
        )
