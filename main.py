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
    i_percent INT,
    m_score INT,
    m_percent INT,
    p_score INT,
    p_percent INT
    )''')

    cursor.execute(table_layout_schema)
    cursor.reset()

    return True

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

    database.close()

def get_user_info():

    name = {}

    name['username'] = input("What is your name: ")

    scores = {"ICT":False, "Maths":False, "Physics":False}

    for item in scores:

        while not scores[item]:

            score_out = input(f"{item} Score 1-100: ")

            try:
                score_out = int(score_out)
                if score_out < 0 or score_out > 100:
                    print("Incorrect range")
                    continue

                scores[item] = score_out
                print(f"You scored {score_out} %")

            except:

                print("Incorrect score")

    output = {**name, **scores}

    return output


def main_loop():

    database_handler()

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

    cursor = database.cursor()

    while True:
        user_info = get_user_info()

        entry = f'''INSERT INTO users (
        name, 
        i_score, 
        i_percent,
        m_score, 
        m_percent, 
        p_score, 
        p_percent
        ) VALUES (
        '{user_info["username"]}', 
        {user_info["ICT"]}, 
        {user_info["ICT"]}, 
        {user_info["Maths"]}, 
        {user_info["Maths"]}, 
        {user_info["Physics"]}, 
        {user_info["Physics"]}
        )'''

        cursor.execute(entry)

        database.commit()

        print("Added entry")

        cursor.reset()

main_loop()
