import socket
import ssl
from cryptography import x509
from cryptography.hazmat.backends.openssl import backend
#from OpenSSL import crypto'''
import pickle
from subprocess import run
from datetime import date,datetime
from db import insert
#import re

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
        self.collectedData['Grade']="A"
        try:
            certpem=ssl.get_server_certificate((self.target,443))
        except:
            print("No ssl certificate found on port 443")
            try:
                certpem=ssl.get_server_certificate((self.target,8080))
            except:
                print("No ssl certificate found on port 8080")
                try:
                    certpem=ssl.get_server_certificate((self.target,80))
                except:
                    print("No ssl certificate found on port 80")
            
        encodedCert=bytes(certpem,'utf-8')
        cert = x509.load_pem_x509_certificate(encodedCert, backend)
        expirey=str(cert.not_valid_after)
        till=datetime.strptime(expirey[:10],"%Y-%m-%d")
        today=date.today()
        now=datetime.strptime(today.strftime("%Y-%m-%d"),"%Y-%m-%d")
        if now>till:
            self.collectedData["Validity"]="Expired "+expirey
            self.points-=10
        else:
            self.collectedData["Valid till"]=expirey
        '''certload=crypto.load_certificate(crypto.FILETYPE_PEM, encodedCert)
        rawData=str(crypto.dump_certificate(crypto.FILETYPE_TEXT,certload).decode('utf-8'))
        self.collectedData["Common Name"]=re.findall("CN=(.*?)\)",str(cert.subject))[0]
        self.collectedData["Serial Number"]=str(cert.serial_number)
        self.collectedData["Valid Till"]=str(cert.not_valid_after)
        self.collectedData["Valid From"]=str(cert.not_valid_before)
        self.collectedData["Public Key"]=cert.public_key().__class__.__name__
        self.collectedData["Issuer"]=re.findall("CN=(.*?)\)",str(cert.issuer))[0]
        #self.collectedData["Signature Algorithm"]=re.findall("Signature Algorithm: (.*?)",rawData)[0]
        self.collectedData["Signature Algorithm"]=cert.signature_hash_algorithm.__class__.__name__
        self.collectedData["Raw Certificate"]=rawData'''
        #output={'Issuer':str(cert.issuer)[1:-1],"Issued To":str(cert.subject)[1:-1],"Validity":str(cert.not_valid_before)+" to "+str(cert.not_valid_after),"Raw Data":str(rawData.decode('utf-8'))}
        run(["nmap --script ssl-enum-ciphers -p80,443,8080 -Pn -oN NmapResults.txt {}".format(self.target)],shell=True)
        with open("NmapResults.txt",'r') as test:
            output=test.read()
        output=output.split('\n')
        for x in output:
            if 'TLSv' in x:
                self.collectedData["Supports {}".format(x[2:-2].lstrip())]=""
                if '1.0' in x or '1.1' in x:
                    self.points-=10
        #print(self.points)
        
        for y in range(len(output)):
            #print(y)
            if 'warnings' in output[y]:
                #index=output.index(y)
                index=y+1
                while('TLSv' not in output[index] and 'least' not in output[index]):
                    #print(output[index])
                    self.warnings+=1
                    self.collectedData['Warning {}'.format(self.warnings)]=output[index][1:].lstrip()
                    self.points-=10
                    index+=1
                '''for warning in output[index+1:-5]:
                    self.collectedData['Warning {}'.format(self.warnings)]=warning[2:].lstrip()
                    self.points-=10'''

        #print(self.points)
        print("Calculating weak ciphers.....")
        weakCount=0
        for g in range(len(output)):
            #print(g)
            if '|     ciphers:' in output[g]:
                index=g+1
                print(index)
                self.collectedData['Weak Ciphers in {}:'.format(output[index-2][2:-2].lstrip())]=""
                protocolIndex=index-2
                while('compressors' not in output[index]):
                    #print("GRade")
                    #print(output[index][-1])
                    if output[index][-1].isalpha() and output[index][-1] !='A':
                        weakCount+=1
                        self.collectedData[output[protocolIndex][1:].strip()+" Weak cipher {}".format(weakCount)]=output[index][1:-4].strip()
                        self.points-=10
                    index+=1
        print(self.points)

        #print(self.points)
        if self.points<=50:
            self.collectedData['Grade']='F'
        elif self.points>50 and self.points<=60:
            self.collectedData['Grade']='E'
        elif self.points>60 and self.points<=70:
            self.collectedData['Grade']='D'
        elif self.points>70 and self.points<=80:
            self.collectedData['Grade']='C'
        elif self.points>80 and self.points<=90:
            self.collectedData['Grade']='B'
        elif self.points>90 and self.points<=100:
            self.collectedData['Grade']='A'
        byteData=pickle.dumps(self.collectedData)
        insert(self.uuid,self.name,self.target,self.timestamp,'sslModule',byteData,self.connection)