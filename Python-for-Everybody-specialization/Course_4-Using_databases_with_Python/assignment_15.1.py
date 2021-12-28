'''
create a SQLITE database or use an existing database and create a table in the database called "Ages":

CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)
Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only
these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Jensyn', 20);
INSERT INTO Ages (name, age) VALUES ('Umaima', 34);
INSERT INTO Ages (name, age) VALUES ('Dara', 36);
INSERT INTO Ages (name, age) VALUES ('Rayhan', 32);
INSERT INTO Ages (name, age) VALUES ('Corran', 40);
INSERT INTO Ages (name, age) VALUES ('Jillian', 37);
Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X

Find the first row in the resulting record set
'''

import sqlite3

db = sqlite3.connect(':memory:')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE Ages ( 
    name VARCHAR(128), 
    age INTEGER
)''')


cursor.execute('''DELETE FROM Ages''')

# Insert users
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Jensyn', 20)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Umaima', 34)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Dara', 36)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Rayhan', 32)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Corran', 40)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Jillian', 37)''')


# Select user
cursor.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')


user1 = cursor.fetchone()
print(f"The first row in the resulting record set : {user1[0]}")

db.commit()
db.close()
