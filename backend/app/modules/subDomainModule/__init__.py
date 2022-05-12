import json
import requests

class subDomainModule:
	def __init__(self,uuid,target):
		self.uuid=uuid
		#self.name=name
		self.target=target
		#self.connection=connection
		#self.timestamp=timestamp
		self.collectedData={}
		
	
	def getDomains(self):
		res=requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": self.target}).json()["subdomains"]
		for x in res:
			self.collectedData[x]=""

	def start(self):
		self.getDomains()
		with open(f"app/past_Scans/{self.uuid}/{self.__class__.__name__}.json","w") as f:
			json.dump(self.collectedData,f)
		'''byteData=pickle.dumps(self.collectedData)
		insert(self.uuid,self.name,self.target,self.timestamp,'subDomainModule',byteData,self.connection)'''

