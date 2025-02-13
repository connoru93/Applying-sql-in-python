import mysql.connector

def add_member(id, name, age):
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
            # SQL query to add a new member
            cursor.execute('''
                INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)
            ''', (id, name, age))
            
            # Commit the changes
            connection.commit()
            print(f"Member added successfully: ID={id}, Name={name}, Age={age}")
    
    except mysql.connector.IntegrityError:
        print(f"Error: Member with ID {id} already exists.")
    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
add_member(1, 'John Doe', 30)
add_member(2, 'Jane Smith', 25)
add_member(1, 'Alice Johnson', 28)  # This should trigger a duplicate ID error