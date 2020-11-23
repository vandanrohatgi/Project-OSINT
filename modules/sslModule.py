import socket
import ssl
from cryptography import x509
from cryptography.hazmat.backends.openssl import backend
from OpenSSL import crypto

def getSSL(target):
    ip=socket.gethostbyname(target)
    certpem=ssl.get_server_certificate((ip,443))
    encodedCert=bytes(certpem,'utf-8')
    
    cert = x509.load_pem_x509_certificate(encodedCert, backend)

    certload=crypto.load_certificate(crypto.FILETYPE_PEM, encodedCert)
    rawData=crypto.dump_certificate(crypto.FILETYPE_TEXT,certload)

    output={'Issuer':cert.issuer,"Issued To":cert.subject,"Validity":str(cert.not_valid_before)+" to "+str(cert.not_valid_after),"Raw Data":rawData.decode('utf-8')}
    return(output)



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