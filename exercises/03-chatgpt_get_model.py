#!/usr/bin/env python3

#import modules
import requests
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

#Perform request
response = requests.request("GET",INT_DATA['url'] + INT_DATA['endpoint_models'], headers=HEADERS)
response_json = response.json()

#List all_models
all_models  = [model["id"] for model in response_json["data"]]
print("\nAll models: ",all_models)

#List all_gtp_models
gpt_models  = [model for model in all_models if model.startswith("gpt")]
print("\nAll GPT models: ",gpt_models)
