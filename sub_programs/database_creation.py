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