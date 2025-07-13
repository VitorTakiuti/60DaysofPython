#connecting to da database
import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

print("Connection estabilished successfully")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Characters (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   Name TEXT NOT NULL,
                   Power INTEGER NOT NULL, 
                   Universe TEXT NOT NULL)
                   """)

print("Table was sucessfully created !")

cursor.execute("""
               INSERT INTO Characters (Name, Power, Universe)
               VALUES ("Goku", 9000, "DragonBall")
               """)
cursor.execute("""
               INSERT INTO Characters (Name, Power, Universe)
               VALUES ("Vegeta", 8000, "DragonBall")
               """)

connection.commit()

print("Data successfully loaded to the table")

connection.close()