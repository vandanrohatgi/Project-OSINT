import os
import json
import pymongo
from bson.objectid import ObjectId
'''def insert(uuid, name, target, timestamp, module, data, connection):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO output VALUES (?,?,?,?,?,?)",
        (uuid, name, target, timestamp, module, data),
    )
    connection.commit()
    return'''


'''if not os.path.exists("./osint.db"):
    connection = sqlite3.connect("osint.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE output (ID varchar,Name varchar ,Target varchar,Time varchar,Module varchar, Data blob)"
    )

if not os.path.exists("past_scans"):
    os.mkdir("past_scans")

if not os.path.exists("past_scans/meta.json"):
    with open("past_scans/meta.json",'w') as f:
        json.dump({},f)

if not os.path.exists("keys.json"):
    keys = {
        "credentials": {"test": "test"},
        "mineLead": "",
        "github": "",
    }
    with open("keys.json", "w") as outfile:
        json.dump(keys, outfile)
'''

class database:
    def __init__(self) -> None:
        mongodb_url=os.environ.get("MONGODB_URL")
        self.client = pymongo.MongoClient(mongodb_url)
        self.db=self.client['SecureApp']

    def put_object(self,object):
        collection=self.db['Scans']
        result=collection.insert_one(object)
        return result.inserted_id
    
    def update_object(self,scan_id,update_data):
        collection=self.db['Scans']
        collection.update_one({"_id":scan_id},{"$set":update_data})
    
    def get_creds(self):
        collection=self.db['credentials']
        return collection.find()
        """for i in collection:
                if i.get('credentials',None)!=None:
                    return i['credentials']"""
    def get_results(self,scan_id=None):
        collection=self.db['Scans']
        formatted_data={}
        if scan_id != None:
            result=collection.find_one({"_id":ObjectId(scan_id)})
            formatted_data[str(result.pop('_id'))]=result
            return formatted_data
        for doc in collection.find():
            formatted_data[str(doc.pop('_id'))]=doc
        return formatted_data
        

'''obj=database()

for i in obj.get_object("credentials").find():
    print(i)'''