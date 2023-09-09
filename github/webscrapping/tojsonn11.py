import json
import sys
from collections import OrderedDict
import csv
import os

with open("/Users/tunab/Downloads/Newfolder/demo/rawdata_n11.json", encoding="utf-8") as json_file:
    data = []
    for d in json_file:
        data.append(json.loads(d.replace(u'\n', u'').replace('  ', '').replace('\t', '').replace(u'\\n', u'').replace('\n', '')))
    with open('/Users/tunab/Downloads/Newfolder/demo/json/n11.json', 'w') as out:
        json.dump(data, out)

