
import requests

facts_str = ''

for i in range(1,4):
        url = "https://catfact.ninja/fact"
        response = requests.get(url)
        data = response.json()
        facts_str += (f"<h{i}>{data['fact']}</h{i}>\n")

print(facts_str)
body_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8|>
    <meta name="viewport" content="width=device-width, initial-scale=1,0">
    <title>Document</title>
</head>
<body>
    {facts_str}
</body>
</html>
"""

with open("cat_facts.html", "w", encoding="utf-8") as file_writer:
    file_writer.write(body_html)


