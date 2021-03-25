import pymongo
import json
import bd_config

#loop over data creating a list of recrods to insert
data_path = "raw_data/cleaned_agdata.json"
record_list = []
with open(data_path, 'r') as f:
    data = json.load(f)
    for state in data:
        for county in data[state]:
            # build a record
            if county == 'id':
                continue
            record = {}
            record['state'] = state
            record['county'] = county
            record['ag_usage'] = {} 
            for usage in data[state][county]:
                record['ag_usage'][usage] = data[state][county][usage]
            # append to list
            record_list.append(record)

#for i in range(10):
#    print(record_list[i])


bd_config.init()
connectTo = "ag_data"

client = pymongo.MongoClient(f"mongodb+srv://{bd_config.USERNAME}:{bd_config.PASSWORD}@bricluster.yskth.mongodb.net/{connectTo}?retryWrites=true&w=majority")
db = client.ag_data

records = db.ag_records

records.insert_many(record_list)

client.close()
