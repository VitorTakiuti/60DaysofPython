import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute("UPDATE Characters SET Power = 9500 WHERE Name = 'Goku'")

connection.commit()

print("Updated Data for Goku")

cursor.close()
connection.close()