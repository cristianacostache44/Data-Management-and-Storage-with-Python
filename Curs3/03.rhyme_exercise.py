
import requests
import json

url = "https://api.datamuse.com/"


param1 = {
    "sl" : "art"                     # same as hardcoding in link as https://api.datamuse.com/words?rel_rhy=beautiful    sl = sounds like
}

param2 = {
    "ml" : "cat"                            # same as hardcoding in link as https://api.datamuse.com/words?ml=woman    ml = means like
}

print(f"Words that sound like {param1['sl']}")
ml = []
response1 = requests.get(f"{url}words", params=param1)
for item in response1.json():
    ml.append(item["word"])
print(ml)

print(f"Words that have a meaning like {param2['ml']}")
sl = []
response2 = requests.get(f"{url}words", params=param2)
for item in response2.json():
    sl.append(item["word"])
print(sl)
