import sqlite3 as sql

db = sql.connect("contacts.sqlite3")
name = input("Enter the name: ")
cursor = db.cursor()
cursor.execute(f"SELECT * FROM contacts WHERE name LIKE '{name}'")
print(cursor.fetchall())


#_____Another Solution______#

for row in cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", (name, )):
    print(row)
    
cursor.close()
db.close()