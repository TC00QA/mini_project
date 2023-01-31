import mysql.connector

from database_creation import database_creation
from table_creation import table_creation

def database_handler():

    try:

        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pa$$w0rd"
        )
    except:
        # Lazy error handling
        print("Failed to connect to database")
        return

    if not database_creation(database):
        print("Error")
        return

    database.close()

    try:

        database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Pa$$w0rd",
            database = "scores"
        )
    except:
        # Lazy error handling
        print("Failed to connect to database")
        return

    if not table_creation(database):
        print("Error creating table")
        return

    return database