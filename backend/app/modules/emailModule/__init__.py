import requests

class emailModule:
	def __init__(self,scan_id,target,db):
		self.target=target
		self.scan_id=scan_id
		self.collectedData={}
		self.db=db
	
	def get_domain_search(self):
		token=[x['mineLead'] for x in self.db.get_creds() if x.get('mineLead',None)][0]
		res=requests.get(f'https://api.minelead.io/v1/search/?domain={self.target}&key={token}')
		return (res.json())

	def start(self):
		apidata=self.get_domain_search()
		try:
			for email in apidata['emails']:
				self.collectedData[email.get('email')]=""
		except KeyError:
			pass
		#return self.collectedData
		self.db.update_object(self.scan_id,{"result":{self.__class__.__name__:self.collectedData}})
