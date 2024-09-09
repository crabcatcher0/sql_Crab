import mysql.connector
from database import DATABASE_NAME, USER, PASSWORD, HOST, PORT



class CrabMysql:


    @classmethod
    def _get_connection(cls):
        """
        Helper method to establish and return a database connection.
        """
        try:
            conn = mysql.connector.connect(
                database=DATABASE_NAME,
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT
            )
            return conn
        except mysql.connector.Error as e:
            print(f"Error connecting to database: {str(e)}")
            return None


    @classmethod
    def _get_cursor(cls, conn):
        """
        Helper method to get a new cursor from the connection.
        """
        if conn and conn.is_connected():
            return conn.cursor()
        else:
            print("Connection is not established or closed.")
            return None


    @classmethod
    def create(cls, model: str, fields: dict):
        """
        Method to create a table.
        """
        conn = cls._get_connection()
        cursor = cls._get_cursor(conn)
        
        if not conn or not cursor:
            print("Unable to proceed without a valid connection and cursor.")
            return

        col_dtype = ", ".join([f"{col} {dtype}" for col, dtype in fields.items()])
        
        try:
            query = f"""
                 CREATE TABLE {model} (
                    {model}_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                    {col_dtype}
                );"""
            cursor.execute(query)
            conn.commit()
            print(f"Table '{model}' created.")

        except mysql.connector.Error as e:
            if e.errno == 1050:
                print(f"Table '{model}' already exists. Skipping....")
            elif e.errno == 2055:
                print("Connection might not be set up properly.")
            else:
                print(f"Error at create: {str(e)}")
                
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
        


    @classmethod
    def add_field(cls, model: str, field: str, data_type):
        conn = cls._get_connection()
        cursor = cls._get_cursor(conn)
        
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
    def delete_item(cls, pk: int):
        conn = cls._get_connection()
        cursor = cls._get_cursor(conn)
        model = cls.__name__.lower()
        try:
            if not conn.is_connected():
                conn.reconnect(attempts=3, delay=2)

            cursor.execute(f"DELETE FROM {model} WHERE {model}_id=%s", (pk,))
            conn.commit()
            print("Data deleted successfully.")
        except Exception as e:
            print(f"Error on delete: {str(e)}")

        finally:
            if conn.is_connected():
                conn.close()


    @classmethod
    def get_object(cls, field: list = None):
        conn = cls._get_connection()
        cursor = cls._get_cursor(conn)
        model = cls.__name__.lower()
        final = [] 
        try:
            if not field:
                query = f"SELECT * from {model};"
            else:
                fields_str = ", ".join(field)
                query = f"SELECT {fields_str} from {model};"

            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                final = [dict(zip(field, row)) for row in result]
                print("Operation success.")

            conn.commit()
        except Exception as e:
            print(f"Error on get: {str(e)}.")
            final = None

        finally:
            conn.close()
        return final
    

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        model = cls.__name__.lower()

        fields = {
            attr: value for attr, value in cls.__dict__.items()
            if not callable(value) and not attr.startswith("__")
        }

        cls.create(
            model=model,
            fields= fields
        )

    


    @staticmethod
    def charField(max_length=255):
        return f"CHAR({max_length})"