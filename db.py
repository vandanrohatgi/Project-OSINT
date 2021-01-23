import sqlite3
import pickle
import os
import json

def insert(uuid,name,target,timestamp,module,data,connection):
	cursor=connection.cursor()
	cursor.execute("INSERT INTO output VALUES (?,?,?,?,?,?)",(uuid,name,target,timestamp,module,data))
	connection.commit()
	return


if not os.path.exists("./osint.db"):
		connection=sqlite3.connect("osint.db")
		cursor=connection.cursor()
		cursor.execute("CREATE TABLE output (ID varchar,Name varchar ,Target varchar,Time varchar,Module varchar, Data blob)")
	
if not os.path.exists("./keys.json"):
	keys={
    	"credentials":{"test":"test"},
    	"snov.io":{
    	    "grant_type":"client_credentials",
    	    "client_id":"",
    	    "client_secret": ""
    	},
    	"github":"",
    	"Censys":{
    	    "API":"",
    	    "secret":""
    	}
		}
	with open("keys.json","w") as outfile:
		json.dump(keys,outfile)