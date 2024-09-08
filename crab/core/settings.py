DATABASE_NAME = 'test.db'

import mysql.connector


class MySQLConnection:
    def __init__(self, database, user, password, host, port):
        self.conn = mysql.connector.connect(
            user = user,
            password = password,
            host = host,
            database = database,
            port = port
        )


    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            print("Query executed successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()


    def fetch_results(self, query, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
        
    
    def close(self):
        self.conn.close()