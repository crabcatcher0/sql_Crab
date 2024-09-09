import mysql.connector
from database import DATABASE_NAME, USER, PASSWORD, HOST, PORT


conn = mysql.connector.connect(
    database = DATABASE_NAME,
    user = USER,
    password = PASSWORD,
    host = HOST,
    port = PORT
)

cursor = conn.cursor()

class CrabMysql:

    @classmethod
    def create(cls, model: str, fields: dict):
        col_dtype = ", ".join([f"{col} {dtype}" for col, dtype in fields.items()])
        try:
            cursor.execute(f"""
                CREATE TABLE {model} (
                    {model}_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                    {col_dtype}
                );
            """)
            print(f"Table '{model}' created.")

        except mysql.connector.Error as e:
            if e.errno == 1050:
                print(f"Table '{model}' already exists. Skipping creation.")
            if e.errno == 2055:
                print(f"Conn might not be setup properly. **Ignore.")

            else:
                print(f"Error at create: {str(e)}")
                
        finally:
            conn.close()


    @classmethod
    def add_field(cls, model: str, field: str, data_type):
        try:
            if data_type is None:
                raise ValueError(f"Data type for field '{field}' cannot be None.")
            
            cursor.execute(f"""
            ALTER TABLE {model.lower()}
            ADD COLUMN {field} {data_type};
            """)
            print(f"Column '{field}' created...")

        except mysql.connector.Error as e:
            if e.errno == 1060:
                print(f"Column '{field}' already exists...Skipping..")
            if e.errno == 2055:
                print(f"Conn might not be setup properly. **Ignore.")

        except Exception as e:
            print(f"Error: {str(e)}.")

        finally:
            if cursor:
                cursor.close()
            if conn.is_connected():
                conn.close()



    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        model = cls.__name__.lower()

        fields = {
            attr: value for attr, value in cls.__dict__.items() if not callable(value)
            and not attr.startswith("__")
        }

        cls.create(
            model=model,
            fields= fields
        )

    


    @staticmethod
    def charField(max_length=255):
        return f"CHAR({max_length})"