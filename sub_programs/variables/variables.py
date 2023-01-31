table_layout_schema = ('''CREATE TABLE users (
ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
name VARCHAR(20), 
i_score INT, 
i_percent INT,
m_score INT,
m_percent INT,
c_score INT,
c_percent INT
)''')

host = "localhost"
user = "root"
password = "Pa$$w0rd"
database_selection = "scores"