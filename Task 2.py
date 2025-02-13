import mysql.connector
from mysql.connector import Error

def create_workout_sessions_table():
    try:
        # Connect to the gym database
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='C@sper12',
            database='gym'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create WorkoutSessions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS WorkoutSessions (
                    session_id INT AUTO_INCREMENT PRIMARY KEY,
                    member_id INT,
                    date DATE NOT NULL,
                    duration_minutes INT NOT NULL CHECK(duration_minutes > 0),
                    calories_burned INT NOT NULL CHECK(calories_burned >= 0),
                    FOREIGN KEY (member_id) REFERENCES Members(id)
                )
            ''')
            print("WorkoutSessions table created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

create_workout_sessions_table()