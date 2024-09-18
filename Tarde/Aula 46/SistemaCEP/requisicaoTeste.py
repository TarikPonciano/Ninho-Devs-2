import requests

resposta = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")

print(resposta.json()["id"])