
import requests

base_url = "https://random.dog/woof"
response1 = requests.get(base_url)
print(response1.text)

url2 = base_url + response1.text
response2 = requests.get(url2)

extensie = response1.text.split(".")[1]

with open(f"random_dog.{extensie}", "wb") as file_writer:
    file_writer.write(response2.content)