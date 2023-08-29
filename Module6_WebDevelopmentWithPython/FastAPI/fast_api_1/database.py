import mysql.connector


def create_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="siva2405",
        database="fastapi1"
    )
    return connection
