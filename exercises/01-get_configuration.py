#!/usr/bin/env python3
#https://docs.python.org/3/library/configparser.html

#Import Modules
import os
import pathlib
import configparser

#Set File paths
APP_PATH    = pathlib.Path(__file__).parents[1].absolute()
CONFIG_FILE = os.path.join(APP_PATH, "config", "configuration.conf")

#Read current Config File and save it on Config Parser obj
CONFIG      = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)

#Read current Config Parser object.
print(CONFIG)
print(CONFIG.sections())
print(CONFIG.items('chatgpt_integration'))
print(dict(CONFIG.items('chatgpt_integration')))


#Convert object to Dictionary
config_dict = {}
for stanza in CONFIG.sections():
   config_dict[stanza] = dict(CONFIG.items(stanza))

#Print current configuration.   
print(config_dict['chatgpt_integration'])
