# convert to csv
import sys
import json
import csv

ifilename = "Yelp Data Files/JSON Files/review.json"
try:
    ofilename = sys.argv[2]
except:
    ofilename = ifilename + ".csv"

# LOAD DATA
json_lines = [json.loads(l.strip()) for l in open(ifilename, encoding="utf8").readlines()]
OUT_FILE = open(ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow(["review_id", "user_id", "business_id", "stars", "date", "text", "useful", "funny", "cool"])
json_no = 0
for l in json_lines:
    root.writerow(
        [l["review_id"], l["user_id"], l["business_id"], l["stars"], l["date"], l["text"], l["useful"], l["funny"],
         l["cool"]])
    json_no += 1

print('Finished {0} lines'.format(json_no))
OUT_FILE.close()
