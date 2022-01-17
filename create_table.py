import sqlite3
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username Text,password text)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text,price real)"
cursor.execute(create_table)
# cursor.execute("INSERT INTO items values ('test',10.99)")
# query = "SELECT * FROM items"
# result = cursor.execute(query)
# row = result.fetchone()
# print(row)
connection.commit()
connection.close()