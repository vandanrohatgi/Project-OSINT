import sqlite3
import pickle
import os

def initialize():
	if os.path.exists("./osint.db"):
		pass
	else:
		connection=sqlite3.connect("osint.db")
		cursor=connection.cursor()
		cursor.execute("CREATE TABLE output (ID varchar,Name varchar ,Target varchar,Time varchar,Module varchar, Data blob)")

def insert(uuid,name,target,timestamp,module,data,connection):
	cursor=connection.cursor()
	cursor.execute("INSERT INTO output VALUES (?,?,?,?,?,?)",(uuid,name,target,timestamp,module,data))
	connection.commit()
	return



'''
cur2=con.cursor()
cur2.execute("select * from output)
list(cur2)
rows=cur2.fetchone() or cur2.fetchall()
'''