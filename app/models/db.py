import json

def read():    
    data = dict

    with open('app/models/db.json', 'r') as jsonfile:
        data = json.load(jsonfile)
    
    return data

def write(element='', data=dict):

    with open('app/models/db.json', 'w') as jsonfile:
        json.dump(data, jsonfile)

