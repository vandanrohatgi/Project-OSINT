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
    scan_id=db.put_object({"name":name,"target":target,"date":date,"time":time,"modules":toImport})

    for i in toImport:
        module_obj=__import__('app.modules.'+i,globals(),locals(),[i])
        objects.append(getattr(module_obj,i)(scan_id,target,db))
    
    for i in objects:
        i.start()
    return


 