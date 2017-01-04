import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# Make a new user
user = (1, 'bob', 'asdf')
insert_query = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query, user)

# Create multiple users
users = [
    (2, 'sam', 'asdf'),
    (3, 'annie', 'asdf')
]

cursor.executemany(insert_query, users)

# Retrieve from database

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
