import json

data = {"monday":"username","tues":"123"}

def writeJSON():
    with open('data.json', 'w+') as outfile:
        json.dump(data, outfile, indent=4)

def readJSON():
    with open("data.json") as file:
        data = json.load(file)