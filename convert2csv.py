#convert to csv
import sys
import json
import csv

ifilename = sys.argv[1]
try:
 ofilename = sys.argv[2]
except:
 ofilename = ifilename + ".csv"

# LOAD DATA
json_lines = [json.loads( l.strip() ) for l in open(ifilename).readlines() ]
OUT_FILE = open(ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow(["business_id","name","address","hours","is_open","categories","city","state","review_count","stars","postal_code","longitude","latitude","attributes"])
json_no = 0
for l in json_lines:
 root.writerow([l["business_id"], l["name"],l["address"],l["hours"],l["is_open"],l["categories"],l["city"],l["state"],l["review_count"],l["stars"],l["postal_code"],l["longitude"],l["latitude"],l["attributes"]])
 json_no += 1

print('Finished {0} lines'.format(json_no))
OUT_FILE.close()