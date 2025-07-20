import sqlite3


conn = sqlite3.connect("StudentDB")

cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME TEXT NOT NULL, 
               AGE INTEGER
               )
''')

print("Table is created")

data = [("Aditya", 21), ("Kunal", 89), ("Kartik", 20)]

# cursor.executemany('''
#     INSERT INTO Students(NAME, AGE) VALUES(? , ? )
# ''', data)

# print("Data inserted")


#UPDATE

#UPDATE TABLE SET AGE = ? WHERE NAME = ?


# cursor.execute('''
#     UPDATE Students SET AGE = ? WHERE NAME = ?
# ''', (19, "Kunal"))

# print("Kunal age is updated")

#Delete
#DELETE FROM TABLE WHERE NAME = ?

cursor.execute('''
    DELETE FROM Students WHERE NAME = ?
''', ("Kunal",))
print("Data deleted")

conn.commit()
conn.close()