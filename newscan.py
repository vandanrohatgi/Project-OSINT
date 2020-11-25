import uuid
from modules import sslModule,portScanModule
import sqlite3

modules=['portScanModule','sslModule','emailModule','publicIpModule','subDomainModule']
#loadedModules={}
toImport=[]
objects=[]

def new(form):
    newID=str(uuid.uuid4())[:8]
    name=form.get('name')
    target=form.get('target')
    for i in modules:
        #loadedModules[i]=form.get(i)
        if form.get(i)!=None:
            toImport.append(i)
    '''for i in loadedModules.keys():
        if loadedModules[i]=='on':
            toImport.append(i)'''
    print(toImport)
    connection=sqlite3.connect("/home/vandan/osint/osint.db")
    for i in toImport:
        obj=__import__('modules.'+i,globals(),locals(),[i])
        objects.append(getattr(obj,i)(newID,name,target,connection))
    
    for i in objects:
        i.start()

