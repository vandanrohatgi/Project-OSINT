import json
import socket
from db import insert
from modules.sslModule.ssllabsscanner import newScan,resultsFromCache
#import re

#https://raw.githubusercontent.com/TrullJ/ssllabs/master/ssllabsscanner.py
class sslModule:
    def __init__(self,uuid,name,target,timestamp,connection):
        self.uuid=uuid
        self.name=name
        self.target=target
        self.connection=connection
        self.timestamp=timestamp
        self.ip=socket.gethostbyname(target)
        self.points=100
        self.collectedData={}
        self.warnings=0

    def start(self):
        self.collectedData=newScan(self.target)
        #self.collectedData=resultsFromCache(self.target)
        with open(f"past_Scans/{self.uuid}/{self.__class__.__name__}.json","w") as f:
            json.dump(self.collectedData,f)
        '''byteData=pickle.dumps(self.collectedData)
        insert(self.uuid,self.name,self.target,self.timestamp,'sslModule',byteData,self.connection)'''