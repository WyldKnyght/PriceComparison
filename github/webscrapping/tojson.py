import json
import sys
from collections import OrderedDict
import csv
import os

with open("/Users/tunab/Downloads/Newfolder/demo/rawdata_gittigidiyor.json", encoding="utf-8") as json_file:
    data = []
    for d in json_file:
        data.append(json.loads(d))
    with open('/Users/tunab/Downloads/Newfolder/demo/json/gittigidiyor.json', 'w') as out:
        json.dump(data, out)
with open("/Users/tunab/Downloads/Newfolder/demo/rawdata_n11.json", encoding="utf-8") as json_file:
    data = []
    for d in json_file:
        data.append(json.loads(d))
    with open('/Users/tunab/Downloads/Newfolder/demo/json/n11.json', 'w') as out:
        json.dump(data, out)
with open("/Users/tunab/Downloads/Newfolder/demo/rawdata_hepsiburada.json", encoding="utf-8") as json_file:
    data = []
    for d in json_file:
        data.append(json.loads(d))
    with open('/Users/tunab/Downloads/Newfolder/demo/json/hepsiburada.json', 'w') as out:
        json.dump(data, out)
with open("/Users/tunab/Downloads/Newfolder/demo/rawdata_amazon.json", encoding="utf-8") as json_file:
    data = []
    for d in json_file:
        data.append(json.loads(d))
    with open('/Users/tunab/Downloads/Newfolder/demo/json/amazon.json', 'w') as out:
        json.dump(data, out)



