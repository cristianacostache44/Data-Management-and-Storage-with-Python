
import requests

url = "https://api.nationalize.io/"
params = {
    "name" : "Cristiana"
}
data = requests.get(url, params = params).json()
countries = data['country']
print(f"Pentru numele - {params['name']}:")
for c in countries:
    print(f"Tara {c['country_id']} are probabilitatea {c['probability']}")
