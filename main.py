import mysql.connector

def database_creation(database):
    cursor = database.cursor()
    cursor.execute("SHOW DATABASES")

    for item in cursor:
        if "scores" in item:
            print("Database Found")
            cursor.reset()
            return True

    print("Database not found, creating")
    cursor.execute("CREATE DATABASE scores")
    cursor.reset()
    return True

def table_creation(database):
    cursor = database.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")
    print("Dropping tables")

    table_layout_schema = ('''CREATE TABLE users (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(20), 
    i_score INT, 
    i_percent VARCHAR(4),
    m_score INT,
    m_percent VARCHAR(4),
    p_score INT,
    p_percent VARCHAR(4)
    )''')

    cursor.execute(table_layout_schema)




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

    table_creation(database)


database_handler()
