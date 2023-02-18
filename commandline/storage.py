#!/usr/bin/env python

import json
from fuzzywuzzy import fuzz

data = {"monday":"username","tues":"123"}

def writeJSON():
    with open('data.json', 'w+') as outfile:
        json.dump(data, outfile, indent=4)

def readJSON():
    with open("data.json") as file:
        data = json.load(file)

# Function to perform fuzzy search on the JSON data
def fuzzy_search(data, query):
    results = []
    for item in data:
        score = fuzz.token_set_ratio(item['name'], query)
        if score >= 60:
            results.append((score, item))
    return results