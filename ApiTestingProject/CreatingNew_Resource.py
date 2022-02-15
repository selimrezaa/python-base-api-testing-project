import json
import requests
import jsonpath

url = "https://reqres.in/api/users"

file = open("C:/Users/SELIM/PycharmProjects/ApiTestingProject/CreateUser.json",'r')
json_input = file.read()

request_json = jsonpath.jsonpath(json_input, "okay")

# make post request input json body

response = requests.post(url, request_json)
print(response.content)

assert response.status_code==204, "dont matching!"