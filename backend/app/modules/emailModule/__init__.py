import json
import requests

#https://emailcrawlr.com/pricing
#https://hunter.io/api
#https://minelead.io

class emailModule:
	def __init__(self,uuid,target,db):
		self.uuid=uuid
		#self.name=name
		self.target=target
		#self.connection=connection
		#self.timestamp=timestamp
		self.collectedData={}
	
	def get_access_token(self):
		with open("keys.json") as keys:
			#params=json.load(keys)['snov.io']
			API_key=json.load(keys)['mineLead']

		#res = requests.post('https://api.snov.io/v1/oauth/access_token', data=params)
		#res=requests.get(f'https://api.minelead.io/v1/search/?domain=www.example.com&key={}&max-emails=5')
		'''resText = res.text.encode('ascii','ignore')
		resText = json.loads(resText)['access_token']
		if resText != '':
			return(resText)
		else:
			print("Please create an account on snov.io and place API keys in the keys.json file")
			return("")
		'''
		if API_key != '':
			return(API_key)
		else:
			print("Please create an account on minelead.io and place API keys in the keys.json file")
			return ""

	
	def get_domain_search(self,token):
		#token = self.get_access_token()
		params = {
		  'access_token': token,
		  'domain': self.target,
		  'type': 'all',
		  'limit': 100,
		  'lastId': 0
		}
		#res = requests.get('https://api.snov.io/v2/domain-emails-with-info', params=params)
		#res=requests.get(f'https://api.minelead.io/v1/search/?domain={self.target}&key={token}&max-emails=5')
		res=requests.get(f'https://api.minelead.io/v1/search/?domain={self.target}&key={token}')
		return (res.json())

	def start(self):
		token=self.get_access_token()
		if token=="":
			print("minelead.io Access token could not be generated")
			return
		apidata=self.get_domain_search(token)
		#print(apidata)
		for email in apidata['emails']:
			#self.collectedData[email.get('email')]=email.get('position',' ')
			self.collectedData[email.get('email')]=""
		with open(f"past_Scans/{self.uuid}/{self.__class__.__name__}.json","w") as f:
			json.dump(self.collectedData,f)
		'''byteData=pickle.dumps(self.collectedData)
		insert(self.uuid,self.name,self.target,self.timestamp,'emailModule',byteData,self.connection)'''
