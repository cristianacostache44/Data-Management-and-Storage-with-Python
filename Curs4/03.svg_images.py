
import requests

url = "https://api.dicebear.com/10.x/lorelei/svg"
response = requests.get(url)

with open("lorelei.svg", "w") as file_writer:
    file_writer.write(response.text)