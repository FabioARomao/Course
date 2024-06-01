import psycopg2

#establishing the connection
conn = psycopg2.connect(database="auth", user='postgres', password='postgres', host='0.0.0.0', port= '5438')
print(conn)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


#Preparing query to create a database
sql = '''CREATE database IF NOT EXISTS auth'''

#Creating a database
sql = '''createdb auth'''

#cursor.execute(sql)
print("Database created successfully........")

#Preparing query to create a tables
sql = '''CREATE TABLE if not exists logins ( \
	id serial PRIMARY KEY, \
	nome VARCHAR ( 120 ) UNIQUE NOT NULL, \
	email VARCHAR ( 150 ) UNIQUE NOT NULL, \
    password VARCHAR ( 256 ) NOT NULL
)'''

#created_on TIMESTAMP NOT NULL,
#last_login TIMESTAMP 

#Creating a table

cursor.execute(sql)
print("Table created successfully........")

#Preparing query to create a users
sql1 = "insert into logins (nome,email,password)values('%s', '%s', '%s')"

#Creating a users
cursor.execute(sql1)
print("Users created successfully........")

#Closing the connection

conn.close()