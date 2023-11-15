# upload to postgresql
import psycopg2

# Replace these values with your own database connection details
dbname = "postgres"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"  # Default PostgreSQL port

create_query = "CREATE TABLE houses (name varchar(100), location varchar(100), image_url varchar(200));"

select_query = "select * from houses;"
 

# Establish a connection to the database
connection = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# cursor.execute("DROP TABLE houses;")
# connection.commit()

# creating database
cursor.execute("""CREATE TABLE IF NOT EXISTS houses (
    name varchar(255),
    location varchar(255),
    url varchar(255)
);""")

insert_command =  """INSERT INTO houses
VALUES ('%s', '%s', '%s')"""

cursor.execute(insert_command % ('first', 'some more', 'value3'))

# cursor.execute("""INSERT INTO tmp
# VALUES ('second', 'more', 'value3')""")

# connection.commit()

cursor.execute("""SELECT * FROM houses""")
myresult = cursor.fetchall()

for name, location, url in myresult:
  print(name)

# # Example: Execute a simple query
# cursor.execute("SELECT version();")
# version = cursor.fetchone()

# cursor.execute('DROP TABLE houses;')
# connection.commit()

# cursor.execute(create_query)
# print("PostgreSQL version:", version)
# cursor.execute(sql);

# cursor.execute(select_query)

# print("Selecting rows from publisher table using cursor.fetchall")

# publisher_records = cursor.fetchall()

# # You can execute more queries here...

if connection:
    cursor.close()
    connection.close()
    print("Connection closed.")
