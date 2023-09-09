import json
import sys
from collections import OrderedDict
import csv
import os
import numpy as np

with open('/Users/tunab/Downloads/Newfolder/demo/rawdata_hepsiburada.json', encoding="utf-8") as f:
    reader=csv.DictReader(f)
    a = []
    for row in f:
        productName=row.split('"productName": "')[1].split('", "price"')[0]
        price=row.split('"price": "')[1].split('", "productLink')[0]
        productLink=row.split('"productLink": "')[1].split('"}')[0]
        req={"PutRequest":
            {
                "Item": {
                "productName": {"S":productName}, 
                "price": {"S":price}, 
                "productLink": {"S":productLink}
                }
            }
        }
        a.append(req)
    with open('/Users/tunab/Downloads/Newfolder/demo/json/hepsiburada.json', 'w') as out:
        a = np.array(a)
        data = {"products":
                a.tolist()}
        json.dump(data, out)

with open('/Users/tunab/Downloads/Newfolder/demo/rawdata_n11.json', encoding="utf-8") as f:
    reader=csv.DictReader(f)
    a = []
    for row in f:
        productName=row.split('"productName": "')[1].split('", "price"')[0]
        price=row.split('"price": "')[1].split('", "productLink')[0]
        productLink=row.split('"productLink": "')[1].split('"}')[0]
        req={"PutRequest":
            {
                "Item": {
                "productName": {"S":productName}, 
                "price": {"S":price}, 
                "productLink": {"S":productLink}
                }
            }
        }
        a.append(req)
    with open('/Users/tunab/Downloads/Newfolder/demo/json/n11.json', 'w') as out:
        a = np.array(a)
        data = {"products":
                a.tolist()}
        json.dump(data, out)
with open('/Users/tunab/Downloads/Newfolder/demo/rawdata_amazon.json', encoding="utf-8") as f:
    reader=csv.DictReader(f)
    a = []
    for row in f:
        productName=row.split('"productName": "')[1].split('", "price"')[0]
        price=row.split('"price": "')[1].split('", "productLink')[0]
        productLink=row.split('"productLink": "')[1].split('"}')[0]
        req={"PutRequest":
            {
                "Item": {
                "productName": {"S":productName}, 
                "price": {"S":price}, 
                "productLink": {"S":productLink}
                }
            }
        }
        a.append(req)
    with open('/Users/tunab/Downloads/Newfolder/demo/json/amazon.json', 'w') as out:
        a = np.array(a)
        data = {"products":
                a.tolist()}
        json.dump(data, out)
with open('/Users/tunab/Downloads/Newfolder/demo/rawdata_gittigidiyor.json', encoding="utf-8") as f:
    reader=csv.DictReader(f)
    a = []
    for row in f:
        productName=row.split('"productName": "')[1].split('", "price"')[0]
        price=row.split('"price": "')[1].split('", "productLink')[0]
        productLink=row.split('"productLink": "')[1].split('"}')[0]
        req={"PutRequest":
            {
                "Item": {
                "productName": {"S":productName}, 
                "price": {"S":price}, 
                "productLink": {"S":productLink}
                }
            }
        }
        a.append(req)
    with open('/Users/tunab/Downloads/Newfolder/demo/json/gittigidiyor.json', 'w') as out:
        a = np.array(a)
        data = {"products":
                a.tolist()}
        json.dump(data, out)




