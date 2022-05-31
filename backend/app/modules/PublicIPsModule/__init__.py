import requests

class PublicIPsModule:
	def __init__(self,scan_id,target,db):
		self.db=db
		self.scan_id=scan_id
		self.target=target
		self.collectedData={}

	def threatCrowd(self):
		res=requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": self.target}).json()["resolutions"]
		for x in res:
			self.collectedData[x.get('ip_address','')]=f"Last Resolved: {x.get('last_resolved','')}"

	def start(self):
		self.threatCrowd()
		#return self.collectedData
		self.db.update_object(self.scan_id,{"result":{self.__class__.__name__:self.collectedData}})
