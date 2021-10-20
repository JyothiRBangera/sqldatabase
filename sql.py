import sqlite3

try:
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
 
 
    print("Successfully Connected to SQLite")
    cur = sqliteConnection.cursor()

 
    for row in cur.execute('SELECT * FROM MOVIE;'):
        print(row)
       

    
    cursor.close()

except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
