import requests

class PublicIPsModule:
	def __init__(self,uuid,target,db):
		self.uuid=uuid
		self.db=db
		self.target=target
		self.IPs={}
		self.collectedData={}
		self.final=[]

	def threatCrowd(self):
		res=requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": self.target}).json()["resolutions"]
		for x in res:
			self.collectedData[x.get('ip_address','')]=f"Last Resolved: {x.get('last_resolved','')}"

	def start(self):
		self.threatCrowd()
		self.db.update_object(self.uuid,{self.__class__.__name__:self.collectedData})
