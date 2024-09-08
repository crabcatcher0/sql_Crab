import mysql.connector


class MySQLConnection:
    def __init__(self, database, user, password, host, port):
        try:
            self.conn = mysql.connector.connect(
                user = user,
                password = password,
                host = host,
                database = database,
                port = port
            )

        except mysql.connector.Error as e:
            print(f"Connection Error: {e}")
            self.conn = None


    def execute_query(self, query, params=None):
        if not self.conn:
            print("MySQL Connection not available.")
            return
        
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            print("Query executed successfully.")

        except mysql.connector.Error as err:
            if err.errno == 1060: 
                print("Duplicate column name. Skipping...")
            elif err.errno == 1050: 
                print("Table already exists. Skipping...")
            else:
                print(f"Database Error: {err}")
        finally:
            if cursor:
                cursor.close()


    def fetch_results(self, query, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
        
    
    def close(self):
        self.conn.close()

    