import sqlite3
import pickle

connection=sqlite3.connect("osint.db")
cursor=connection.cursor()
cursor.execute("CREATE TABLE output (ID varchar,Name varchar ,Target varchar,Time varchar,Module varchar, Data blob)")

'''
cur2=con.cursor()
cur2.execute("select * from output)
list(cur2)
rows=cur2.fetchone() or cur2.fetchall()
'''