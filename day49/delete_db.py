import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute("DELETE FROM Characters WHERE Name = 'Vegeta'")

connection.commit()

print("Character Vegeta was deleted successfully")

cursor.close()
connection.close()
