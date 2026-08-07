
import requests
from selenium.webdriver import Edge

url = "https://uigradients.com/"
response = requests.get(url)

with open("index.html", "wb") as file_writer:
    file_writer.write(response.content)

browser = Edge()
browser.get(url)

with open("index_selenium.html", "w", encoding="utf-8") as file_writer:
    file_writer.write(browser.page_source)

with open("index_selenium.html","r") as file_reader:
    html = file_reader.read()
    parts = html.split('<span class="hex__name">')
    color_parts = parts[1:]
    print(f"Colors for gradient are: {color_parts[0][:7]} and {color_parts[1][:7]}")


input("To exit press enter")
browser.quit()