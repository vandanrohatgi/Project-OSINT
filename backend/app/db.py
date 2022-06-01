import os
import pymongo
from bson.objectid import ObjectId

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
        collection.update_one({"_id":scan_id},{"$addToSet":update_data})
    
    def get_creds(self):
        collection=self.db['credentials']
        return collection.find()

    def get_results(self,scan_id=None,limit=0,meta=False):
        collection=self.db['Scans']
        formatted_data={}
        if scan_id != None:
            result=collection.find_one({"_id":ObjectId(scan_id)})
            formatted_data[str(result.pop('_id'))]=result
            return formatted_data
        if meta:
            for doc in collection.find().limit(limit):
                doc.pop('result')
                formatted_data[str(doc.pop('_id'))]=doc
            return formatted_data
        for doc in collection.find().limit(limit):
            formatted_data[str(doc.pop('_id'))]=doc
        return formatted_data