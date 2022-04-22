import json
import uuid
from datetime import datetime
import os

modules=['portScanModule','sslModule','emailModule','subDomainModule','allPortScanModule','PublicIPsModule','gitHubModule']
#domain=['portScanModule','sslModule','emailModule','subDomainModule','allPortScanModule','PublicIPsModule','s3bucketModule']
#keyword=['gitHubModule']

'''def isDomain(target):
    regex = "^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)[A-Za-z]{2,6}"
    p = re.compile(regex)
    if(re.search(p, target)):
        return True
    else:
        return False'''

def new(form):
    toImport=[]
    objects=[]
    '''params=form.split('&')
    name=params[0][5:]
    target=params[1][7:]'''
    time=str(datetime.now().strftime("%I:%M:%S %p"))
    date=str(datetime.now().strftime("%d/%b/%Y"))
    name=form['name']
    target=form['target']
    toImport=form['modules']
    newID=str(uuid.uuid4())[:8]
    os.mkdir(f"past_scans/{newID}")
    #os.makedirs(f"past_scans/{newID}")
    #if isDomain(target):
    '''for i in modules:
            if i in form:
                toImport.append(i)
    #else:'''
    #    toImport=keyword
    #connection=sqlite3.connect("./osint.db")
    with open("past_scans/meta.json","r") as f:
        meta_data=json.load(f)
        meta_data[newID]={"name":name,"target":target,"time":time,"date":date,"modules":toImport}
    with open("past_scans/meta.json","w") as f:
        json.dump(meta_data,f)
    
    for i in toImport:
        #obj=__import__('modules.'+i,globals(),locals(),[i])
        module_obj=__import__('modules.'+i,globals(),locals(),[i])
        #objects.append(getattr(module_obj,i)(newID,name,target,timestamp,connection))
        objects.append(getattr(module_obj,i)(newID,name,target,time,date))
    
    for i in objects:
        i.start()
    return


 