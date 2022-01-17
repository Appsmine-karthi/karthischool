import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE users (id int,username text,password text)"
cursor.execute(create_table)
user = (1,"karthi","1234")
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)
users=[(2,"kannan","1234"),(3,"Elakiya","1234")]
cursor.executemany(insert_query,users)
select_squery = "SELECT * FROM users"
for row in cursor.execute(select_squery):
    print(row)
connection.commit()
connection.close()