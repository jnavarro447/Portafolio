import requests
from models import Gender, Role

url = "http://localhost:8000/api/v1/users"

newUser = {
    "firstName": "menganito",
    "lastName": "Perez",
    "gender": "male",
    "roles": ["user"]
    }
newUser2 = {
    "firstName": "joaquin",
    "lastName": "lopez",
    "middleName": "ricardo",
    "gender": "female",
    "roles": ["admin"]
}


postRequest = requests.post(url, json=newUser)
# postRequest2 = requests.post(url, json=newUser2)

print(f"Status code: {postRequest.status_code}")
print(f"Text: {postRequest.text}")
# print(f"Status code: {postRequest2.status_code}")
# print(f"Text: {postRequest2.text}")

