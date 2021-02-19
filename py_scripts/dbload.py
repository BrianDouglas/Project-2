import pymongo
import bd_config

bd_config.init()
connectTo = "agData"

client = pymongo.MongoClient(f"mongodb+srv://{bd_config.USERNAME}:{bd_config.PASSWORD}@bricluster.yskth.mongodb.net/{connectTo}?retryWrites=true&w=majority")
db = client.test

db.create_collection

#db.collection.find({}, {"_id": False})

