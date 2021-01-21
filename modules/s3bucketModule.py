import pickle
from db import insert
from subprocess import run
import re
import os

class s3bucketModule:
	def __init__(self,uuid,name,target,timestamp,connection):
		self.uuid=uuid
		self.name=name
		self.target=target
		self.connection=connection
		self.timestamp=timestamp
		self.collectedData={}
	
	
	def start(self):
		run(["./modules/slurpdir/runthis.sh",self.target])
		f=open("./modules/slurpdir/slurp.txt","r")
		data=f.read()
		f.close()
		try:
			run(["rm","./modules/slurpdir/slurp.txt"])
		except:
			print("slurp.txt does not exist")
		try:
			for x in re.findall("Requests200List:\[(.*?)\]",data)[0].split(' '):
				self.collectedData[x]="200"
		except:
			self.collectedData["INFO"]="No S3 Data Found"
		try:
			for x in re.findall("Requests403List:\[(.*?)\]",data)[0].split(' '):
				self.collectedData[x]="403"
		except:
			self.collectedData["INFO"]="No S3 Data Found"
		byteData=pickle.dumps(self.collectedData)
		insert(self.uuid,self.name,self.target,self.timestamp,'s3bucketModule',byteData,self.connection)
