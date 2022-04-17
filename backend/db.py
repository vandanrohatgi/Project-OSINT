import sqlite3
import pickle
import os
import json


'''def insert(uuid, name, target, timestamp, module, data, connection):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO output VALUES (?,?,?,?,?,?)",
        (uuid, name, target, timestamp, module, data),
    )
    connection.commit()
    return'''


'''if not os.path.exists("./osint.db"):
    connection = sqlite3.connect("osint.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE output (ID varchar,Name varchar ,Target varchar,Time varchar,Module varchar, Data blob)"
    )'''

if not os.exists("./past_scans/meta.json"):
    os.mkdir("past_scans")
    with open("past_scans/meta.json") as f:
        json.dump({},f)

if not os.path.exists("./keys.json"):
    keys = {
        "credentials": {"test": "test"},
        "mineLead": "",
        "github": "",
    }
    with open("keys.json", "w") as outfile:
        json.dump(keys, outfile)
