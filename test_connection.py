from database.connection import create_connection

connection = create_connection()

if connection:
    print("🎉 Database connection successful!")

    connection.close()

    print("🔒 Connection closed.")