import mysql.connector
from mysql.connector import Error

def connect_to_database():
    db_name = "python"
    user = "root"
    password = "C@sper12"
    host = "127.0.0.1"  # Corrected the comma to a dot

    try:
        # Establish a connection to the database
        conn = mysql.connector.connect(
            database=db_name,  # Use the variable for the database name
            user=user,          # Use the variable for the username
            password=password,  # Use the variable for the password
            host=host           # Use the variable for the host
        )
        
        if conn.is_connected():
            print("Connected to the database.")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None


connection = connect_to_database()


if connection:
    connection.close()
    print("Connection closed.")