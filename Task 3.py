import mysql.connector

def update_member_age(member_id, new_age):
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
            
            # Check if the member exists
            cursor.execute('SELECT * FROM Members WHERE id = %s', (member_id,))
            member = cursor.fetchone()
            
            if member is None:
                print(f"Error: Member with ID {member_id} does not exist.")
                return
            
            # SQL query to update the age of the member
            cursor.execute('''
                UPDATE Members 
                SET age = %s 
                WHERE id = %s
            ''', (new_age, member_id))
            
            # Commit the changes
            connection.commit()
            print(f"Member ID {member_id} age updated to {new_age}.")
    
    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
update_member_age(1, 31)  # Update age for member ID 1
update_member_age(3, 25)  # Attempt to update age for a non-existent member