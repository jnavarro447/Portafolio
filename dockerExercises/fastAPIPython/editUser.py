import requests

url = "http://127.0.0.1:8000/api/v1/users/"
userID = "6378ccc2-dd83-48f5-99a4-b58552a34d7f"

toChange = {
    "middleName": "Vazquez",
    "roles": ["student", "admin"]
}

putRequest = requests.put(url+userID, json=toChange)

print(f"Status code: {putRequest.status_code}")
