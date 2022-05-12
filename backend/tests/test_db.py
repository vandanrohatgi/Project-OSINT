import pymongo
import os

def test_db_url():
    mongodb_url=os.environ.get("MONGODB_URL")
    client = pymongo.MongoClient(mongodb_url)
    db = client.test
    assert db != None