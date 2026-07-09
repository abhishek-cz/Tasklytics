import mysql.connector
from mysql.connector import Error

from database.config import (
    HOST,
    USER,
    PASSWORD,
    DATABASE,
    PORT
)


def create_connection():
    """
    Creates and returns a MySQL database connection.
    """

    try:

        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            port=PORT
        )

        if connection.is_connected():
            print("✅ Connected to Tasklytics Database")

        return connection

    except Error as e:
        print(f"❌ Database Connection Error: {e}")
        return None