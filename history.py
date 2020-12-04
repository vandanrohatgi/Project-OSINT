import sqlite3
import pickle
import json

def retrieve(uuid=None,data=None):
    connection=sqlite3.connect("/home/vandan/osint/osint.db")
    connection.row_factory=sqlite3.Row
    cursor=connection.cursor()
    if uuid==None and data==None:    
        cursor.execute("select distinct ID,Name,Target,Time from output")
        rows=cursor.fetchall()
        return(rows)
    elif uuid!=None and data==None:
        modules=[]
        cursor.execute("select * from output where ID=?",(uuid,))
        rows=cursor.fetchall()
        head=[rows[0]['ID'],rows[0]['Name'],rows[0]['Target'],rows[0]['Time']]
        for i in rows:
            modules.append(i['Module'])
        resultList=[head,modules]
        return(resultList)
    else:
        cursor.execute("select data from output where ID=? and module=?",(uuid,data))
        row=cursor.fetchone()
        Data=pickle.loads(row['Data'])
        return(json.dumps(Data))


        
#retrieve('27c9d478','sslModule')