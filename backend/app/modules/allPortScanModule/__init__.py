import json
import socket
import threading
from queue import Queue
import uuid

class portScanModule:
    def __init__(self,uuid,target,db):
        #self.name=name
        self.target=target
        self.uuid=uuid
        #self.connection=connection
        #self.timestamp=timestamp
        #self.date=date
        #self.ports={}
        self.lock=threading.Lock()
        self.q=Queue()
        self.collectedData={}
        self.db=db
        #socket.setdefaulttimeout(1)

    def scan(self,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.ip,int(port)))   
            with self.lock:
                self.collectedData[str(port)]="Open"
                print(f"{port} is open")
            sock.close()
                #self.ports.update({str(self.ip)+':'+str(port):'open'})
        except:
            pass
    def threader(self):
        while True:
            port=self.q.get()
            self.scan(port)
            self.q.task_done()
    
    def start(self):
        try:
            self.ip=socket.gethostbyname(self.target)
        except:
            print("cannot resolve domain")
            return

        for x in range(100):
            t=threading.Thread(target=self.threader)
            t.daemon=True
            t.start()
        for port in range(1,65535):
            self.q.put(port)
        
        self.q.join()
        #print(self.collectedData)
        #byteData=pickle.dumps(self.collectedData)
        self.db.update_object(self.uuid,{self.__class__.__name__:self.collectedData})
        """with open(f"app/past_Scans/{self.uuid}/{self.__class__.__name__}.json","w") as f:
            json.dump(self.collectedData,f)"""
        #insert(self.uuid,self.name,self.target,self.timestamp,'PortScanModule',byteData,self.connection)

