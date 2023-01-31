import mysql.connector

from sub_programs.database_creation import database_creation
from sub_programs.table_creation import table_creation

from sub_programs.variables.variables import host, user, password, database_selection

def database_handler():

    # Trys to connect to database (No selection)

    try:

        database = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

    except:
        # Lazy error handling
        print("Failed to connect to database\n")
        return

    # Connect to DB and see if scores exists, if not, create

    if not database_creation(database):
        print("Error creating 'scores'\n")
        return

    # Close current connection

    database.close()

    # ReOpen connection referencing the scores database

    try:

        database = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database_selection
        )
    except:
        # Lazy error handling
        print("Failed to connect to database \n")
        return

    # Drop tables and re-create

    if not table_creation(database):
        print("Error creating table \n")
        return

    return database