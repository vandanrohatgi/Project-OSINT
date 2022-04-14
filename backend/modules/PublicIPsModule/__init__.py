import json
import requests
import pickle
from db import insert

#https://search.censys.io/api
class PublicIPsModule:
	def __init__(self,uuid,name,target,timestamp,connection):
		self.uuid=uuid
		self.name=name
		self.target=target
		self.connection=connection
		self.timestamp=timestamp
		self.IPs={}
		self.collectedData={}
		self.final=[]

	def censys(self,api,secret):
		url='https://censys.io/api/v1'
		query={"query":self.target,'fields':["ip"],}

		res=requests.post(url=url+"/search/ipv4",auth=(api,secret),data=json.dumps(query))
		pages=res.json()['metadata']['pages']

		for y in range(1,pages+1):
			query={'query':self.target,'fields':["ip"],'page':y,}
			res=requests.post(url=url+"/search/ipv4",auth=(api,secret),data=json.dumps(query))
			result=res.json()['results']
			for x in result:
				self.collectedData[x.get('ip'," ")]=" "

		'''filtered=[x.get('ip') for x in result]
			self.collectedData[]
			self.final+=filtered

		for x in self.final:
			self.IPs[x]=""'''

	def threatCrowd(self):
		res=requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": self.target}).json()["resolutions"]
		for x in res:
			self.collectedData[x.get('ip_address','')]=f"Last Resolved: {x.get('last_resolved','')}"
			#self.collectedData[x.get('ip_address'," ")]=" "
		'''self.final=[x.get("ip_address") for x in res]
		for x in self.final:
			self.IPs[x]=""'''

	def start(self):
		'''with open("keys.json") as keys:
			data=json.load(keys)
			api=data["Censys"]["API"]
			secret=data["Censys"]["secret"]
		if api ==" " or secret ==" ":
			print("Kindly provide the Censys API key and secret key")
			return'''
		#self.censys(api,secret)
		self.threatCrowd()
		byteData=pickle.dumps(self.collectedData)
		insert(self.uuid,self.name,self.target,self.timestamp,'getPublicIPsModule',byteData,self.connection)
