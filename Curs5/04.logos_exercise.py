
import requests

base_url = "https://logotypes.dev"

brands = ["Python", "Github", "Apple"]
brands_svg = ''
for brand in brands:
    response = requests.get(f"{base_url}/{brand}")
    data = response.text
    brands_svg += f"<li>{data}</li>"
# print(brands_svg)

body_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8|>
    <meta name="viewport" content="width=device-width, initial-scale=1,0">
    <title>Document</title>
</head>
<body>
    <ol>{brands_svg}</ol>
</body>
</html>
""" 

with open("logos_ordered.html", "w") as file_writer:
    file_writer.write(body_html)