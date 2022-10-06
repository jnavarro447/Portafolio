import requests

url = "http://localhost:8000/api/v1/users/"
userID = "84c0db9c-06db-43ee-82eb-8969ace79df0"

deleteRequest = requests.delete(url+userID)

print(f"requestDelete Status code: {deleteRequest.status_code}")

