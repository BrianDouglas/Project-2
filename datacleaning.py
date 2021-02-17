import csv

path = "raw_data/agdata by county.csv"

STATE_NAME = 5
STATE_NUM = 6
COUNTY_NAME = 9
COUNTY_NUM = 10
VALUE = 19

clean_dict = {}

with open(path) as csvfile:
    reader = csv.reader(csvfile)
    count = 1
    next(reader)
    for row in reader:
        if count > 8:
            count = 1
        if count%2 == 0:
            count += 1
            continue
        else:
            try:
                acres = int(row[VALUE].replace(",",""))
            except:
                acres = 0
            count += 1
            if row[STATE_NAME] in clean_dict:
                if row[COUNTY_NAME] in clean_dict[row[STATE_NAME]]:
                    clean_dict[row[STATE_NAME]][row[COUNTY_NAME]].append(acres) 
                else:
                    clean_dict[row[STATE_NAME]][row[COUNTY_NAME]] = [acres]
            else:
                clean_dict[row[STATE_NAME]] = {row[COUNTY_NAME]: [acres]}
            
#print(clean_dict["ALABAMA"])

state_totals = {}
for state in clean_dict:
    print(state)
    total_acres = 0
    for county in clean_dict[state]:
        total_acres += sum(clean_dict[state][county])
    state_totals[state] = total_acres

print(state_totals)

