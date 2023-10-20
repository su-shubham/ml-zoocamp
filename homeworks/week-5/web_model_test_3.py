import requests

url = "http://localhost:8080/risk"

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url, json=client).json()

print(response)
