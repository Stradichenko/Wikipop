#!/usr/bin/python3

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

SEARCHWORD = "Buckling spring"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": SEARCHWORD,
    "srlimit": "max" # max is 500
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print"WORD:", SEARCHWORD, "\n"

if DATA['query']['search'][0]['title'] == SEARCHWORD:
    print"Own entry: yes\n"
    counter=0
    for i in DATA['query']['search']:
        counter+=1
    print"Number of entries for this word: ", counter
else:
    print("Own entry: no")
totalhits = DATA['query']['searchinfo']['totalhits']
print "\nTotal hits: ", totalhits, "\n"

