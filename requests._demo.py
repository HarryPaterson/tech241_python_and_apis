import requests
import json

# GET request

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req) # Response [200]
print(post_codes_req.status_code) # 200
print(print(post_codes_req.content)) # returns content from url, as ytes
print(post_codes_req.json()) # turns content into Python dict
print(type(post_codes_req.json())) # shows the type is now dict

# POST request - sending data to the API

json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())

# Pokemon api

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/eevee")
print(pokemon_req.json())

# BBC webpages

bbc_request = requests.get("https://www.bbc.co.uk/")
print(bbc_request.content)



