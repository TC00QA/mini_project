from sub_programs.variables.variables import table_layout_schema

def table_creation(database):

    try:

        cursor = database.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")

        print("Dropping tables\n")

    except:
        #Lazy error handling
        return False

    try:

        cursor.execute(table_layout_schema)
        cursor.reset()

        return True

    except:
        #Lazy error handling
        return False