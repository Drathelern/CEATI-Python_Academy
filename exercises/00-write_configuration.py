#!/usr/bin/env python3
#https://docs.python.org/3/library/configparser.html

#Import Modules
import os
import pathlib
import configparser

#Set File paths
APP_PATH    = pathlib.Path(__file__).parents[1].absolute()
CONFIG_PATH = os.path.join(APP_PATH, "config")
CONFIG_FILE = os.path.join(CONFIG_PATH, "configuration.conf")

#Validate if not existe and create Config Path.
if not os.path.isdir(CONFIG_PATH):
  os.makedirs(CONFIG_PATH)

#Read current Config File and save it on Config Parser obj
CONFIG      = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)

#Set new values
integration_data = {
  'api_key'      : '',
  'organization' : '',
  'url'          : 'https://api.openai.com/',
  'endpoint'     : '/v1/chat/completions',
  'model'        : 'gpt-4o'
}

#set new value to Config parser object
CONFIG['chatgpt_integration']  = integration_data

#Write the new config on the config file
with open(CONFIG_FILE, 'w') as configfile:
  CONFIG.write(configfile)

