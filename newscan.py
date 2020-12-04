import uuid
import sqlite3
from datetime import datetime

modules=['portScanModule','sslModule','emailModule','publicIpModule','subDomainModule','allPortScanModule']
#loadedModules={}

def new(form):
    toImport=[]
    objects=[]
    params=form.split('&')
    name=params[0][5:]
    target=params[1][7:]
    timestamp=str(datetime.now())
    newID=str(uuid.uuid4())[:8]
    '''name=form.get('name')
    target=form.get('target')'''
    for i in modules:
        if i in form:
            toImport.append(i)
    '''    loadedModules[i]=form.get(i)
        if form.get(i)!=None:
            toImport.append(i)
    for i in loadedModules.keys():
        if loadedModules[i]=='on':
            toImport.append(i)'''
    connection=sqlite3.connect("/home/vandan/osint/osint.db")
    for i in toImport:
        obj=__import__('modules.'+i,globals(),locals(),[i])
        objects.append(getattr(obj,i)(newID,name,target,timestamp,connection))
    
    for i in objects:
        i.start()
    return("Scan Complete")

