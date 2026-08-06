
import requests

url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
data_dict = response.json()

new_url = data_dict['message']
new_response = requests.get(new_url)
new_dog_file = new_url.rsplit("/", 1)[-1]

with open(new_dog_file,"wb") as file_writer:
    file_writer.write(new_response.content)
