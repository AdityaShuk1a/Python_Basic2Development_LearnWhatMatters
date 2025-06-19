import sqlite3


'''
INSERT
UPDATE
SELECT
CREATE
DELETE
'''



connection = sqlite3.connect("NewDatabase")

cur = connection.cursor()


#create a new table in the database
'''
datatypes in sqlite 
1. TEXT
2. INTEGER
3. BLOB
4. NULL
'''
cur.execute("CREATE TABLE IF NOT EXISTS newTable( name TEXT, age INTEGER)")

data = [("RAM", 34), ("Lakshman", 29), ("Kartik", 55)]

# cur.executemany('''INSERT INTO newTable(name, age) VALUES (?, ?)
# ''', data)

cur.execute("SELECT * FROM newTable")

'''
fetchone()
fetchall()
fetchmany(2)
'''

print("query executed successfully")
fetchData = cur.fetchall()

for items in fetchData:
    print(items[0])


connection.commit()
connection.close()