
import requests

url = "https://www.link-academy.com"
response = requests.get(url)
print(response)
print(response.status_code) # 100 = informational, 200 = ok successful, 300 = redirection,  400 = client error
print(response.content) # type bytes
print(response.text) # type str

with open("04.requests.html", "w+", encoding = "utf-8") as f_w:
    url = "https://www.link-academy.com"
    response = requests.get(url)
    f_w.write(response.text)
