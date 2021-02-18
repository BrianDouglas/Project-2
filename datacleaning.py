import csv
import json

path = "raw_data/agdata by county.csv"

STATE_NAME = 5
STATE_NUM = 6
COUNTY_NAME = 9
COUNTY_NUM = 10
DATA_ITEM = 16
VALUE = 19


items = [('AG LAND, CROPLAND - ACRES','crop_acres'), 
        ('AG LAND, CROPLAND - NUMBER OF OPERATIONS','crop_ops'),
        ('AG LAND, PASTURELAND - ACRES', 'pasture_acres'),
        ('AG LAND, PASTURELAND - NUMBER OF OPERATIONS','pasture_ops'),
        ('AG LAND, WOODLAND - ACRES','woodland_acres'),
        ('AG LAND, WOODLAND - NUMBER OF OPERATIONS', 'woodland_ops'), 
        ('AG LAND, WOODLAND, PASTURED - ACRES','wood-pasture_acres'), 
        ('AG LAND, WOODLAND, PASTURED - NUMBER OF OPERATIONS','wood-pasture_ops')]

def map_name(row_name):
    for i in range(len(items)):
        if row_name == items[i][0]:
            return items[i][1]
    print(row_name)

discover_data = []
clean_dict = {}
with open(path) as csvfile:
    reader = csv.reader(csvfile)
    count = 1
    next(reader)
    for row in reader:
        # if count > 8:
        #     count = 1
        # if count%2 == 0:
        #     count += 1
        #     continue
        # else:
        if row[DATA_ITEM] not in discover_data:
            discover_data.append(row[DATA_ITEM])
        try:
            current_value = int(row[VALUE].replace(",",""))
        except:
            current_value = 0
        if row[STATE_NAME] in clean_dict:
            if row[COUNTY_NAME] in clean_dict[row[STATE_NAME]]:
                clean_dict[row[STATE_NAME]][row[COUNTY_NAME]][map_name(row[DATA_ITEM])] = current_value 
            else:
                clean_dict[row[STATE_NAME]][row[COUNTY_NAME]] = {map_name(row[DATA_ITEM]): current_value}
        else:
            clean_dict[row[STATE_NAME]] = {row[COUNTY_NAME]: {map_name(row[DATA_ITEM]): current_value}}
            
#print(clean_dict["ALASKA"])
'''with open("raw_data/cleaned_agdata.json", "w") as f:
    json.dump(clean_dict,f,indent=4)'''

state_totals = {}
for state in clean_dict:
    total_acres = 0
    for county in clean_dict[state]:
        for data in clean_dict[state][county]:
            if data.split("_")[1] == 'acres':
                total_acres += clean_dict[state][county][data]
    state_totals[state] = total_acres
print(state_totals)
# print(len(state_totals))
# print(state_totals.keys())

'''path = "raw_data/stateLevelGeo.json"
output_path = "raw_data/acres_stateLevelGeo.json"
with open(path, 'r') as f:
    data = json.load(f)
    for feature in data["features"]:
        if feature["properties"]["NAME"].upper() in state_totals:
            feature["properties"]["ACRES"] = state_totals[feature["properties"]["NAME"].upper()]
    
with open(output_path, 'w') as f:
    json.dump(data,f,indent=4)
'''

# massachutes, conneticut, vermont, new hampshire, rhode island