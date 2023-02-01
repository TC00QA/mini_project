from sub_programs.database_handler import database_handler
from sub_programs.info_gather import get_user_info

def main_loop():

    print("\n")

    database = database_handler()

    cursor = database.cursor()

    while True:


        # Data validation happens in get_user_info()
        #Returns Dictionary
        user_info = get_user_info()

        entry = f'''INSERT INTO users (
        name, 
        i_score, 
        i_percent,
        m_score, 
        m_percent, 
        c_score, 
        c_percent
        ) VALUES (
        '{user_info["username"]}', 
        {user_info["ICT"]}, 
        {user_info["ICT"]}, 
        {user_info["Maths"]}, 
        {user_info["Maths"]}, 
        {user_info["Chemistry"]}, 
        {user_info["Chemistry"]}
        )'''

        cursor.execute(entry)
        database.commit()

        print("Added entry \n")

        cursor.reset()

main_loop()
