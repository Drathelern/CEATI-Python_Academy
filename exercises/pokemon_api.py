#!/usr/bin/env python3
import requests

BASE_URL    = "https://pokeapi.co"
EDNPOINT    = "/api/v2/pokemon/"
POKEMON     = "mewtwo"
URL         = f"{BASE_URL}{EDNPOINT}{POKEMON}"

def list_moves(response_data):
    moves = [cur_move["move"]["name"] for cur_move in response_data["moves"]]

    return moves

def validate_response_code(response_code):
    if response_code >= 200 and response_code < 400:
        print("Request success.\n")
    else:
       raise("Request Failed")

def perform_request(url):
    response      = requests.request("GET", url)
    status_code   = response.status_code
    response_json = response.json()

    return status_code, response_json

if __name__ == '__main__':
  try:
    response_code, response_json = perform_request(URL)
    validate_response_code(response_code)
  except:
    print("Error while requesting")

  pokemon_moves = list_moves(response_json)

  print(*pokemon_moves, sep='\n')