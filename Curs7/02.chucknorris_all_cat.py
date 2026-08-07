
import requests
import json
import pandas as pd

base_url = "https://api.chucknorris.io/jokes/"
categories_url = base_url + "categories"
particular_cat_url = base_url + "random?category="
response_categories = requests.get(categories_url).json() # e o lista

jokes_based_on_cat = {}

# ------- Varianta 1 = printare clasica

for category in response_categories:
    response = requests.get(particular_cat_url+category)
    jokes_based_on_cat[category] = response.json()['value']
#print(jokes_based_on_cat)

# ------- Varianta 2 = creare de fisier si utilizare json

with open("all_jokes_chucknorris.json","w") as fw:
    json.dump(jokes_based_on_cat,fw)

# ------- Varianta 3 = utilizare pandas

df = pd.DataFrame(jokes_based_on_cat.values(), index=jokes_based_on_cat.keys())
df.to_csv("jokes_cat.csv")

# continuam exercitiul 
# facem cate o pagina html pt fiecare gluma din dictionar

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {navi}
    {content}
</body>
</html>"""

navigation = "<nav>"
for category in response_categories:
    navigation += f'<a href="/website/{category}.html"> {category.title()} </a>'
navigation += "</nav>"
base_html = base_html.replace("{navi}", navigation)

for category in response_categories:
    with open(f"website/{category}.html", "w") as fw:
        fw.write(base_html.replace("{content}",f"<h1>{jokes_based_on_cat[category]}</h1>"))

