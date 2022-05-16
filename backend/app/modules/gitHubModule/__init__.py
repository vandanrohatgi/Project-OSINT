
import requests
from urllib import parse
from time import sleep

class gitHubModule:
	def __init__(self,uuid,target,db):
		self.uuid=uuid
		self.db=db
		self.target=target
		self.collectedData={}
		self.url='https://api.github.com/search/code?q='
		self.gitResult='<a href="https://github.com/search?q={}&type=code" target="_blank" rel="noopener noreferrer">{}</a>'

	def search(self,dork,header):
		url_encodedDork=parse.quote(dork)
		r=requests.get(self.url+url_encodedDork,headers=header)
		try:
			if r.json()['total_count']!=0:
				self.collectedData[self.gitResult.format(url_encodedDork,dork)]=str(r.json()['total_count'])
		except:
			pass

	def start(self):
		token=[x['github'] for x in self.db.get_creds() if x.get('github',None)][0]
		header={"Authorization":"token "+token}
		count=0
		current=0
		with open("app/modules/gitHubModule/gitDorks/alldorks.txt") as alldorks:
			dorks=alldorks.read()
		dorks=dorks.split("\n")
		while current<len(dorks):
			if count<30:
				self.search(dorks[current]+" "+self.target,header)
				current+=1
				count+=1
			else:
				print("Sleeping...")
				sleep(60)
				count=0
		self.db.update_object(self.uuid,{self.__class__.__name__:self.collectedData})
