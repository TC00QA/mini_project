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