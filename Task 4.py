import mysql.connector

def delete_workout_session(session_id):
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
            
            # Check if the workout session exists
            cursor.execute('SELECT * FROM WorkoutSessions WHERE session_id = %s', (session_id,))
            session = cursor.fetchone()
            
            if session is None:
                print(f"Error: Workout session with ID {session_id} does not exist.")
                return
            
            # SQL query to delete the workout session
            cursor.execute('DELETE FROM WorkoutSessions WHERE session_id = %s', (session_id,))
            
            # Commit the changes
            connection.commit()
            print(f"Workout session ID {session_id} deleted successfully.")
    
    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
delete_workout_session(1)  # Attempt to delete workout session with ID 1
delete_workout_session(99)  # Attempt to delete a non-existent workout session