import sqlite3
import pickle
from db import insert
from subprocess import run
from os import path

class subDomainModule:
	def __init__(self,uuid,name,target,timestamp,connection):
		self.uuid=uuid
		self.name=name
		self.target=target
		self.connection=connection
		self.timestamp=timestamp
		self.collectedData={}
		self.tools=['amass.txt','subfinder.txt','sublister.txt','assetfinder.txt']
	
	def scan(self):
		try:
			run(['amass','enum','-d',self.target,'-oA','amass.txt'])
		except:
			print("Please install amass")
		try:
			run(['subfinder','-d',self.target,'-v','-all','-t','100','-o','subfinder.txt'])
		except:
			print("Please install subfinder")
		try:
			run(['sublist3r.py','-t','25','-d',self.target,'-o','sublister.txt'])
		except:
			print("Please install sublist3r")
		try:
			run(['assetfinder --subs-only {} > assetfinder.txt'.format(self.target)],shell=True)
		except:
			print("Please install assetfinder")

	def combine(self):
		#check if all the output files are present
		for name in self.tools:
			if not path.exists(name):
				self.tools.remove(name)
		#combine results
		for name in self.tools:
			run(["cat {} >> subdomains.txt".format(name)],shell=True)
		#Remove duplicates
		run(["cat subdomains.txt | sort | uniq > final.txt"],shell=True)
		#cleanup
		for name in self.tools:
			run(["rm",name])	
		run(["rm","subdomains.txt"])
	
	def getDomains(self):
		with open("final.txt",'r') as lines:
			unclean=lines.read()
		clean=unclean.split('\n')
		for x in clean:
			self.collectedData[x]=''

	def start(self):
		#main code
		self.scan()
		self.combine()
		self.getDomains()
		byteData=pickle.dumps(self.collectedData)
		insert(self.uuid,self.name,self.target,self.timestamp,'subDomainModule',byteData,self.connection)

