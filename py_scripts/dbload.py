import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:<password>@bricluster.yskth.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
