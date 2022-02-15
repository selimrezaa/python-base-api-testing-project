import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response.status_code)

assert response.status_code == 200, "error"