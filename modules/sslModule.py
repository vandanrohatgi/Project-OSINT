import socket
import ssl
from cryptography import x509
from cryptography.hazmat.backends.openssl import backend
from OpenSSL import crypto
import pickle
import sqlite3
from db import insert

class sslModule:
    def __init__(self,uuid,name,target,timestamp,connection):
        self.uuid=uuid
        self.name=name
        self.target=target
        self.connection=connection
        self.timestamp=timestamp
        self.ip=socket.gethostbyname(self.target)

    def start(self):
        certpem=ssl.get_server_certificate((self.ip,443))
        encodedCert=bytes(certpem,'utf-8')
        cert = x509.load_pem_x509_certificate(encodedCert, backend)
        certload=crypto.load_certificate(crypto.FILETYPE_PEM, encodedCert)
        rawData=crypto.dump_certificate(crypto.FILETYPE_TEXT,certload)
        output={'Issuer':str(cert.issuer)[1:-1],"Issued To":str(cert.subject)[1:-1],"Validity":str(cert.not_valid_before)+" to "+str(cert.not_valid_after),"Raw Data":str(rawData.decode('utf-8'))}

        byteData=pickle.dumps(output)
        insert(self.uuid,self.name,self.target,self.timestamp,'sslModule',byteData,self.connection)
        '''cursor=self.connection.cursor()
        cursor.execute("INSERT INTO output VALUES (?,?,?,?,'sslModule',?)",(self.uuid,self.name,self.target,self.timestamp,byteData))
        self.connection.commit()'''


'''con=sqlite3.connect("/home/vandan/osint/osint.db")
obj=sslModule('123','test','grocio.in',con)
obj.start()'''


'''ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=target) as s:
        s.connect((target, 443))
        cert = s.getpeercert(True)
    demcert=ssl.DER_cert_to_PEM_cert(cert)'''

'''subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
issuer = dict(x[0] for x in cert['issuer'])
issued_by = issuer['commonName']
print(issued_to,issued_by)'''