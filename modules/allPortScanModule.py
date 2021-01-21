import socket
import threading
import pickle
from queue import Queue
from db import insert

class allPortScanModule:
    def __init__(self,uuid,name,target,timestamp,connection):
        self.name=name
        self.target=target
        self.uuid=uuid
        self.connection=connection
        self.timestamp=timestamp
        self.ports={}
        self.lock=threading.Lock()
        self.q=Queue()
        self.collectedData={}

    def scan(self,port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self.ip,int(port)))   
            sock.close()
            with self.lock:
                self.collectedData[self.ip]=str(port)
                #self.ports.update({str(self.ip)+':'+str(port):'open'})
        except socket.error:
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
        for port in range(1,65000):
            self.q.put(port)
        
        self.q.join()

        byteData=pickle.dumps(self.ports)
        insert(self.uuid,self.name,self.target,self.timestamp,'allPortScanModule',byteData,self.connection)











