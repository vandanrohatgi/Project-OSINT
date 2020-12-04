import socket
import threading
import sqlite3
import pickle
from queue import Queue

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

    def scan(self,port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self.ip,int(port)))   
            sock.close()
            with self.lock:
                self.ports.update({str(self.ip)+':'+str(port):'open'})
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
            cursor=self.connection.cursor()
            cursor.execute("INSERT INTO output VALUES (?,?,?,?,'allPortScanModule',?)",(self.uuid,self.name,self.target,self.timestamp,''))
            self.connection.commit()
            return

        for x in range(100):
            t=threading.Thread(target=self.threader)
            t.daemon=True
            t.start()
        for port in range(1,65000):
            self.q.put(port)
        
        self.q.join()

        byteData=pickle.dumps(self.ports)
        cursor=self.connection.cursor()
        cursor.execute("INSERT INTO output VALUES (?,?,?,?,'allPortScanModule',?)",(self.uuid,self.name,self.target,self.timestamp,byteData))
        self.connection.commit()











