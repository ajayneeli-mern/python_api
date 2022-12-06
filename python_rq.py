import requests
import json

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

querystring = {"ingr":"apple"}

headers = {
	"X-RapidAPI-Key": "a9f165a07bmshe5b57916181a1cfp1e0362jsn3eb0d376b453",
	"X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response = response.json()
for i in response.get("hints"):
    print(i.get("food").get("label"))
