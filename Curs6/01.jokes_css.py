
import requests

base_url = "https://v2.jokeapi.dev/joke/"

jokes_list = []
jokes_topic = ["Christmas","Programming","Dark"]
for topic in jokes_topic:
    data = requests.get(f"{base_url}{topic}").json()
    print(data)
    if data["type"] == "single":
        jokes_list.append(data["joke"])
    else:
        jokes_list.append(f"{data['setup']} {data['delivery']}")


base_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .christmas {{ background-color:red;}}
        .programming {{ background-color:blue;}}
        .dark {{ background-color:darkgreen;}}
    </style>
</head>
<body>
    <div class="christmas">{jokes_list[0]}</div>
    <div class="programming">{jokes_list[1]}</div>
    <div class="dark">{jokes_list[2]}</div>
</body>
</html>"""

with open("jokes.html", "w") as fw:
    fw.write(base_html)