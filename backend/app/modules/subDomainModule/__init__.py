import requests

class subDomainModule:
	def __init__(self,scan_id,target,db):
		self.db=db
		self.target=target
		self.scan_id=scan_id
		self.collectedData={}
		
	
	def getDomains(self):
		res=requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": self.target}).json()["subdomains"]
		for x in res:
			self.collectedData[x]=""

	def start(self):
		self.getDomains()
		#return self.collectedData
		self.db.update_object(self.scan_id,{"result":{self.__class__.__name__:self.collectedData}})