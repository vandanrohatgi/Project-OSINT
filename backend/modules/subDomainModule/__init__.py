import pickle
from db import insert
import requests

class subDomainModule:
	def __init__(self,uuid,name,target,timestamp,connection):
		self.uuid=uuid
		self.name=name
		self.target=target
		self.connection=connection
		self.timestamp=timestamp
		self.collectedData={}
		
	
	def getDomains(self):
		res=requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": self.target}).json()["subdomains"]
		for x in res:
			self.collectedData[x]=""

	def start(self):
		self.getDomains()
		byteData=pickle.dumps(self.collectedData)
		insert(self.uuid,self.name,self.target,self.timestamp,'subDomainModule',byteData,self.connection)

