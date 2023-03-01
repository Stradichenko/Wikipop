#!/usr/bin/python3

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

SEARCHWORD = "Buckling spring"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": SEARCHWORD,
    "prop": "links",
    "pllimit": "max"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

counter = 0

for k, v in PAGES.items():
    for l in v["links"]:
        counter+=1
        print (l["title"]).encode("utf8")
print "Total related words: ", counter

print(DATA)