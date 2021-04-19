import requests
import json

print("GET /v1/hello")
print(requests.get("http://localhost:8080/v1/hello").content)
print("--------")
print("POST /v1/echo")
print(requests.post("http://localhost:8080/v1/echo", json={"test": "sample message"}).content)