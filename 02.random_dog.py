
import requests

url = "https://random.dog"
response = requests.get(url)

with open("dog_page.html","w+", encoding="utf-8") as file_writer:
    file_writer.write(response.text)