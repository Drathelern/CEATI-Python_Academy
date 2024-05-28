#!/usr/bin/env python3

#import modules
import requests

#Set request data
API_KEY     = ""
ORG         = ""

BASE_URL    = "https://api.openai.com"
EDNPOINT    = "/v1/models"

HEADERS     = {
                "Authorization": f"Bearer {API_KEY}",
                "OpenAI-Organization": ORG,
                "Content-Type": "application/json"
              }

#Perform request
response = requests.request("GET",BASE_URL + EDNPOINT, headers=HEADERS)
status_code = response.status_code

#Print statys code 
print(status_code)

#Validate if the request was sucess or failed.
if status_code >= 200 and status_code < 400:
    print("Request success")
else:
    print("Request Failed")
    