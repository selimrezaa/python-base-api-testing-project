import requests

url = "https://reqres.in/api/users?page=2"

res = requests.get(url)
#print response
# print(res)
# print(res.content)
print(res.headers)
