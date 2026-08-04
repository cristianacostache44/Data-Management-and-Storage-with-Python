
import requests

url = "https://random.dog/66b9ea90-1493-4ddc-ab9b-f2b87385e196.mp4"
response = requests.get(url)

with open("dog_video.mp4","wb") as file_writer: # wb = write binary (mp4 nu este o imagine efectiva ci un binar)
    file_writer.write(response.content)