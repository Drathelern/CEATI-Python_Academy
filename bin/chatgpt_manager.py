#!/usr/bin/env python3
import os
import sys
import json
import pathlib
import requests

APP_PATH      = pathlib.Path(__file__).parents[1].absolute()
BIN_PATH      = os.path.join(APP_PATH, "bin")
SCRIPTS_PATH  = os.path.join(BIN_PATH, "scripts")
CONFIG_PATH   = os.path.join(APP_PATH, "config")

sys.path.append(SCRIPTS_PATH)
import utility

class chatGPT_Manager(object):

  @utility.err_handling_decorator
  def __init__(self,config_path, prompt, rol="user"):
    '''
    This method is in charge of initializing all the information necessary for the execution of the manager, retrieving it from the configuration.conf file.\n
    Arguments:
        prompt: prompt to be requested to chatGPT
        rol: the posture which chatGPT will take to process the prompt and respond, the default value is "user".
        config_path: path to the configuration file with the information required for communication with chatGPT
    ''' 
    self.prompt             = prompt
    self.rol                = rol

    configuration_data      = utility.get_config_file_data(config_path)
    integration_data        = configuration_data["chatgpt_integration"]
    self.api_key            = integration_data["api_key"]
    self.organization       = integration_data["organization"]
    self.base_url           = integration_data["url"]
    self.endpoint           = integration_data["endpoint"]
    self.model              = integration_data["model"]
    self.url                = self.base_url + self.endpoint

  @utility.err_handling_decorator
  def get_request_headers(self):
    '''
    This method returns the headers and data needed to make the request to Chatgpt;\n
    Required data:
      Api Key and Organization configured in configuration.conf
      , Rol and Prompt entered when executing the script
    ''' 
    headers  = {
            "Authorization": "Bearer {}".format(self.api_key),
            "OpenAI-Organization": self.organization,
            "Content-Type": "application/json"
          }

    data      = {
            "model": self.model,
            "messages": [{"role": self.rol, "content": self.prompt}]
          }
    
    return headers, data
  
  @utility.err_handling_decorator
  def perform_chatGPT_prompt(self, url):
    '''
    This method performs the request to chatGPT to obtain a response to the prompt.\n
    Arguments:
        URL: openAI URL configured in configuration.conf 
    ''' 
    headers, data   = self.get_request_headers()
    response        = requests.request("POST",url, headers=headers, data=json.dumps(data))
    status_code     = response.status_code
    response_json   = response.json()

    return response_json
  
  @utility.err_handling_decorator
  def list_chatpgt_responses(self, response):
    '''
    This method extracts all messages from ChatGPT and returns them as a list.\n
    Arguments:
        response: chatGPT Response
    ''' 
    response_list = []
    for genai_response in response['choices']:
      response_list.append(genai_response["message"]['content'])

    return response_list

  @utility.err_handling_decorator
  def main(self):
    '''
    This method is the main method which is in charge of sending the request to chatGPT and returning the response as a list.
    ''' 
    chatGPT_response = self.perform_chatGPT_prompt(self.url)
    list_responses   = self.list_chatpgt_responses(chatGPT_response)

    return list_responses

