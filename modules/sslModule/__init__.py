import json
import socket
import ssl
from cryptography import x509
from cryptography.hazmat.backends.openssl import backend
#from OpenSSL import crypto'''
import pickle
from subprocess import run
from datetime import date,datetime
from db import insert
from modules.sslModule.ssllabsscanner import newScan,resultsFromCache
#import re
import time

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
        byteData=pickle.dumps(self.collectedData)
        insert(self.uuid,self.name,self.target,self.timestamp,'sslModule',byteData,self.connection)