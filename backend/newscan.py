import uuid
import sqlite3
from datetime import datetime
import re

modules=['portScanModule','sslModule','emailModule','subDomainModule','allPortScanModule','PublicIPsModule','gitHubModule']
#domain=['portScanModule','sslModule','emailModule','subDomainModule','allPortScanModule','PublicIPsModule','s3bucketModule']
#keyword=['gitHubModule']

def isDomain(target):
    regex = "^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)[A-Za-z]{2,6}"
    p = re.compile(regex)
    if(re.search(p, target)):
        return True
    else:
        return False

def new(form):
    toImport=[]
    objects=[]
    params=form.split('&')
    name=params[0][5:]
    target=params[1][7:]
    timestamp=str(datetime.now())
    newID=str(uuid.uuid4())[:8]
    #if isDomain(target):
    for i in modules:
            if i in form:
                toImport.append(i)
    #else:
    #    toImport=keyword
    connection=sqlite3.connect("./osint.db")
    for i in toImport:
        #obj=__import__('modules.'+i,globals(),locals(),[i])
        module_obj=__import__('modules.'+i,globals(),locals(),[i])
        objects.append(getattr(module_obj,i)(newID,name,target,timestamp,connection))
    
    for i in objects:
        i.start()
    return("Scan Complete")


 