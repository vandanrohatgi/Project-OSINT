import socket
import ssl
from cryptography import x509
from cryptography.hazmat.backends.openssl import backend
from OpenSSL import crypto
import pickle
from db import insert
import re

class sslModule:
    def __init__(self,uuid,name,target,timestamp,connection):
        self.uuid=uuid
        self.name=name
        self.target=target
        self.connection=connection
        self.timestamp=timestamp
        self.ip=socket.gethostbyname(target)
        self.collectedData={}

    def start(self):
        certpem=ssl.get_server_certificate((self.ip,443))
        encodedCert=bytes(certpem,'utf-8')
        cert = x509.load_pem_x509_certificate(encodedCert, backend)
        certload=crypto.load_certificate(crypto.FILETYPE_PEM, encodedCert)
        rawData=str(crypto.dump_certificate(crypto.FILETYPE_TEXT,certload).decode('utf-8'))
        self.collectedData["Common Name"]=re.findall("CN=(.*?)\)",str(cert.subject))[0]
        self.collectedData["Serial Number"]=str(cert.serial_number)
        self.collectedData["Valid From"]=str(cert.not_valid_before)
        self.collectedData["Valid Till"]=str(cert.not_valid_after)
        self.collectedData["Public Key"]=cert.public_key().__class__.__name__
        self.collectedData["Issuer"]=re.findall("CN=(.*?)\)",str(cert.issuer))[0]
        #self.collectedData["Signature Algorithm"]=re.findall("Signature Algorithm: (.*?)",rawData)[0]
        self.collectedData["Signature Algorithm"]=cert.signature_hash_algorithm.__class__.__name__
        self.collectedData["Raw Certificate"]=rawData
        #output={'Issuer':str(cert.issuer)[1:-1],"Issued To":str(cert.subject)[1:-1],"Validity":str(cert.not_valid_before)+" to "+str(cert.not_valid_after),"Raw Data":str(rawData.decode('utf-8'))}
        byteData=pickle.dumps(self.collectedData)
        insert(self.uuid,self.name,self.target,self.timestamp,'sslModule',byteData,self.connection)