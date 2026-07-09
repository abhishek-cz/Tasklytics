import bcrypt
import mysql.connector

from database.connection import create_connection


# ==========================================================
# REGISTER USER
# ==========================================================

def register_user(name, email, password):

    connection = create_connection()

    if connection is None:
        return False, "Database connection failed."

    cursor = connection.cursor()

    try:

        # ------------------------------------------
        # Check if Email Already Exists
        # ------------------------------------------

        cursor.execute(
            """
            SELECT user_id
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        if cursor.fetchone():

            return False, "Email already registered."

        # ------------------------------------------
        # Hash Password
        # ------------------------------------------

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # ------------------------------------------
        # Insert User
        # ------------------------------------------

        cursor.execute(
            """
            INSERT INTO users
            (
                name,
                email,
                password_hash
            )
            VALUES
            (
                %s,
                %s,
                %s
            )
            """,
            (
                name,
                email,
                hashed_password
            )
        )

        user_id = cursor.lastrowid

        # ------------------------------------------
        # Create Default Progress
        # ------------------------------------------

        cursor.execute(
            """
            INSERT INTO user_progress
            (
                user_id
            )
            VALUES
            (
                %s
            )
            """,
            (user_id,)
        )

        # ------------------------------------------
        # Create Default Settings
        # ------------------------------------------

        cursor.execute(
            """
            INSERT INTO user_settings
            (
                user_id
            )
            VALUES
            (
                %s
            )
            """,
            (user_id,)
        )

        # ------------------------------------------
        # Commit Everything Together
        # ------------------------------------------

        connection.commit()

        return True, "Registration Successful!"

    except mysql.connector.Error as err:

        connection.rollback()

        return False, f"Database Error: {err}"

    finally:

        cursor.close()
        connection.close()


# ==========================================================
# LOGIN USER
# ==========================================================

def login_user(email, password):

    connection = create_connection()

    if connection is None:
        return False, "Database connection failed.", None

    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        user = cursor.fetchone()

        if user is None:

            return False, "Invalid Email or Password.", None

        password_match = bcrypt.checkpw(
            password.encode("utf-8"),
            user["password_hash"].encode("utf-8")
        )

        if not password_match:

            return False, "Invalid Email or Password.", None

        return True, "Login Successful!", user

    except mysql.connector.Error as err:

        return False, f"Database Error: {err}", None

    finally:

        cursor.close()
        connection.close()