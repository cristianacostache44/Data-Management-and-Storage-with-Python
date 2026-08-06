
import requests
import json

BASE_URL = "https://icanhazdadjoke.com/"
headers1 = {
    "Accept" : "application/json"
}

headers2 = {
    "Accept" : "text/plain"
}

response1 = requests.get(BASE_URL,headers=headers1)
print(response1.text)

response2 = requests.get(BASE_URL,headers=headers2)
print(response2.text)

response_dict = response1.json()
joke_id = response_dict["id"]
response3 = requests.get(f"https://icanhazdadjoke.com/j/{joke_id}.png", headers=headers1)

with open(f"joke_{joke_id}.png","wb") as file_writer:
    file_writer.write(response3.content)