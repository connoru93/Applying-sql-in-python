import mysql.connector
from mysql.connector import Error

def create_database_and_table():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='C@sper12'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS gym")
            cursor.execute("USE gym")
            
            # Create Members table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Members (
                    id INT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INT NOT NULL CHECK(age > 0)
                )
            ''')
            print("Database and table created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

create_database_and_table()