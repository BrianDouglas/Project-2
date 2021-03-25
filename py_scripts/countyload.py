# file size issues resolved.

import json

data_path = "raw_data/cleaned_agdata.json"
geo_path = "raw_data/countyLevelGeo.json"

id_county_acres = {}
with open(data_path, 'r') as f:
    ag_data = json.load(f)
    total_acres = 0
    for state in ag_data:
        cur_id = ag_data[state]['id']
        cur_name = state
        id_county_acres[cur_id] = {}
        id_county_acres[cur_id]['state name'] = state
        for county in ag_data[state]:
            if county == 'id':
                continue
            total_acres = 0
            for data in ag_data[state][county]:
                #print(f'{state} {county} {data}')
                if data.split("_")[1] == 'acres':
                    total_acres += ag_data[state][county][data]
            id_county_acres[cur_id][county] = total_acres
#print(id_county_acres['02'])
count = 0
with open(geo_path, 'r') as geo_f:
    geo_data = json.load(geo_f)
    for feature in geo_data["features"]:
        cur_id = feature["properties"]["STATE"]
        cur_county = feature["properties"]["NAME"].upper()
        if cur_id in id_county_acres:
            if cur_county in id_county_acres[cur_id]:
                count += 1
                feature["properties"]["ACRES"] = id_county_acres[cur_id][cur_county]
                feature["properties"]["STATE NAME"] = id_county_acres[cur_id]['state name']

#print(count)
#print(geo_data["features"][0]["properties"])


### TALK ABOUT THIS ###
'''
output_path = "raw_data/acres_countyLevelGeo.json"
with open(output_path, 'w') as f:
    json.dump(geo_data,f,indent=1)
'''
