import json
import sys
from collections import OrderedDict
import csv
import os

with open("/Users/tunab/Downloads/Newfolder/demo/rawdata_hepsiburada.json", encoding="utf-8") as json_file:
    data = []
    for d in json_file:
        data.append(json.loads(d))
    with open('/Users/tunab/Downloads/Newfolder/demo/json/hepsiburada.json', 'w') as out:
        json.dump(data, out)

