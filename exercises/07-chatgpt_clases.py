#!/usr/bin/env python3
import os
import pathlib
import utility

APP_PATH      = pathlib.Path(__file__).parents[1].absolute()
CONFIG_PATH   = os.path.join(APP_PATH, "config")
CONFIG_FILE   = os.path.join(CONFIG_PATH, "configuration.conf")

class chatGPT_Manager(object):
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

  def display_init_data(self):
    print("\nPrompt:", self.prompt)
    print("\nBase URL:", self.base_url)
    print("\nEndpoint:", self.endpoint)
    print("\nModel:", self.model)
    print("\nURL:", self.url)
    

chatgpt_manager  = chatGPT_Manager(CONFIG_FILE, "What is Python")
chatgpt_manager.display_init_data()
