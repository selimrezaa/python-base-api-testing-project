import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

jsonResponse = json.loads(response.text)
# print(jsonResponse)

pages = jsonpath.jsonpath(jsonResponse, "total_pages")
print(pages)