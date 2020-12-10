import sqlite3
import json
import requests
import pickle
from db import insert

class getPublicIPsModule:
	def __init__(self,uuid,name,target,timestamp,connection):
		self.uuid=uuid
		self.name=name
		self.target=target
		self.connection=connection
		self.timestamp=timestamp
		self.censysAPI='0e545594-a41d-49b3-999c-c108191e86d5'
		self.censysSecret='7voDPoidQaSdusxoFBLV92Pp3zsLTFgw'
		self.IPs={}
		self.final=[]
	
	def censys(self):
		url='https://censys.io/api/v1'
		query={"query":self.target,'fields':["ip"],}

		res=requests.post(url=url+"/search/ipv4",auth=(self.censysAPI,self.censysSecret),data=json.dumps(query))
		#res=requests.get(url=url+"view/ipv4/htmedia.in")
		pages=res.json()['metadata']['pages']

		try:
			for y in range(1,pages+1):
				query={'query':self.target,'fields':["ip"],'page':y,}
				res=requests.post(url=url+"/search/ipv4",auth=(self.censysAPI,self.censysSecret),data=json.dumps(query))
				result=res.json()['results']
				filtered=[x.get('ip') for x in result]
				self.final+=filtered
		except:
			for x in self.final:
				self.IPs[x]=""

	def threatCrowd(self):
		res=requests.get("http://www.threatcrowd.org/searchApi/v2/domain/report/", {"domain": self.target}).json()["resolutions"]
		self.final=[x.get("ip_address") for x in res]
		for x in self.final:
			self.IPs[x]=""

	def start(self):
		#self.censys()
		self.threatCrowd()
		byteData=pickle.dumps(self.IPs)
		insert(self.uuid,self.name,self.target,self.timestamp,'getPublicIPsModule',byteData,self.connection)
		'''cursor=self.connection.cursor()
		cursor.execute("INSERT INTO output VALUES (?,?,?,?,'getPublicIPsModule',?)",(self.uuid,self.name,self.target,self.timestamp,byteData))
		self.connection.commit()'''

'''obj=getPublicIPs(None,None,"htmedia.in",None,None)
obj.start()
print(obj.IPs)'''