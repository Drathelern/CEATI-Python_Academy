#!/usr/bin/env python3

#import modules
import requests
import json
import utility

#Get the Integration data
CONFIG_DATA = utility.get_config_file_data("configuration.conf")
INT_DATA    = CONFIG_DATA['chatgpt_integration']

#Set Headers and Data
HEADERS     = {
                "Authorization"       : f"Bearer {INT_DATA['api_key']}",
                "OpenAI-Organization" : INT_DATA['organization'],
                "Content-Type"        : "application/json"
              }

DATA        = {
                "model"    : INT_DATA['model'],
                "messages" : [{"role": "user", "content": "What is Python?"}]
              }

response        = requests.request("POST", INT_DATA['url'] + INT_DATA['endpoint'], headers=HEADERS, data=json.dumps(DATA))
response_json   = response.json()

#Display all genAI reposonses
for genai_response in response_json['choices']:
  print("GenAI Response:\n\n{}".format(genai_response["message"]['content']))