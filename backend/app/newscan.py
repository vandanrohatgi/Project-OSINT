from datetime import datetime

modules=['portScanModule','sslModule','emailModule','subDomainModule','allPortScanModule','PublicIPsModule','gitHubModule']


def new(form,db):
    toImport=[]
    objects=[]
    time=str(datetime.now().strftime("%I:%M:%S %p"))
    date=str(datetime.now().strftime("%d/%b/%Y"))
    name=form['name']
    target=form['target']
    toImport=form['modules']
    scan_id=db.put_object({"name":name,"target":target,"date":date,"time":time,"modules":toImport,"result":[]})

    for i in toImport:
        module_obj=__import__('app.modules.'+i,globals(),locals(),[i])
        objects.append(getattr(module_obj,i)(target,db))
    
    for i in objects:
        result=i.start()
        db.update_object(scan_id,{"result":{i.__class__.__name__:result}})
    return


 