import requests
import json

API_KEY = "enter x-rapidapi-key"

url = "https://irctc-indian-railway-pnr-status.p.rapidapi.com/getPNRStatus/{Your PNR Number}"

headers = {
    "x-rapidapi-key": "enter x-rapidapi-key",
    "x-rapidapi-host": "irctc-indian-railway-pnr-status.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Headers:", response.headers)
print(json.dumps(response.json(), indent=2))