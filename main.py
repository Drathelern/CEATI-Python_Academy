#!/usr/bin/env python3

import os
import sys
import pathlib

APP_PATH      = pathlib.Path(__file__).parent.absolute()
BIN_PATH      = os.path.join(APP_PATH, "bin")
CONFIG_PATH   = os.path.join(APP_PATH, "config")
CONFIG_FILE   = os.path.join(CONFIG_PATH, "configuration.conf")

sys.path.append(BIN_PATH)
from chatgpt_manager import chatGPT_Manager

if __name__ == '__main__':
  prompt = input("Prompt to ChatGPT: ")

  chatgpt_manager  = chatGPT_Manager(CONFIG_FILE, prompt)
  chatgpt_response = chatgpt_manager.main()

  print("\n\nResponse:\n")
  print(chatgpt_response[0])