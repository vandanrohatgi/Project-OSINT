import socket
import threading
import pickle
from db import insert

class portScanModule:
    def __init__(self,uuid,name,target,timestamp,connection):
        self.name=name
        self.target=target
        self.uuid=uuid
        self.connection=connection
        self.timestamp=timestamp
        self.commonPorts=['21', '22', '23', '25', '53', '79', '80', '81', '88', '110', '111','113', '119', '123',
             '137', '138', '139', '143', '161', '179','389', '443', 
            '445', '465', '512', '513', '514', '515', '3306',
            '5432', '1521', '2638', '1433', '3389', '5900', '5901', '5902','5903', '5631', '631',
            '636','990', '992', '993', '995', '1080', '8080', '8888', '9000']
        self.collectedData={}
        self.lock=threading.Lock()
        self.threads=[]

    def scan(self,port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #sock.settimeout(10)
            sock.connect((self.ip,int(port)))   
            sock.close()
            with self.lock:
                self.collectedData[str(self.ip)]=port
                #self.ports.update({str(self.ip)+':'+port:'open'})
        except socket.error:
            pass
        

    def start(self):
        try:
            self.ip=socket.gethostbyname(self.target)
        except:
            print("cannot resolve domain")
            return
            
        for x in range(len(self.commonPorts)):
            self.threads.append(threading.Thread(target=self.scan,args=(self.commonPorts[x],)))
            self.threads[x].start()
        for x in range(len(self.commonPorts)):
            self.threads[x].join()

        byteData=pickle.dumps(self.collectedData)
        insert(self.uuid,self.name,self.target,self.timestamp,'PortScanModule',byteData,self.connection)














'''os.system("nmap -T4 -Pn --open {} | grep open | cut -d' ' -f1 | cut -d'/' -f1 > ports.txt".format(target))
if (os.path.exists('ports.txt')):
    f=open('ports.txt','r')
    ports=f.read()
    f.close()
    os.remove('ports.txt')
    print(ports)
else:
    return None'''











