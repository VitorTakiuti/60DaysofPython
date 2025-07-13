import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Characters")

Characters = cursor.fetchall()

print("Characters: ")
for character in Characters:
    print(character)
    
cursor.close()
connection.close()