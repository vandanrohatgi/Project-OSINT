from app.modules.sslModule.ssllabsscanner import newScan


#https://raw.githubusercontent.com/TrullJ/ssllabs/master/ssllabsscanner.py

class sslModule:
    def __init__(self,target,db):
        self.db=db
        self.target=target
        self.collectedData={}
        self.warnings=0

    def start(self):
        self.collectedData=newScan(self.target)
        return self.collectedData
		#self.db.update_object(self.uuid,{self.__class__.__name__:self.collectedData})