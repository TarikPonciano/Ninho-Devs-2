import requests

resposta = requests.get("https://viacep.com.br/ws/60410692/json/")
print(resposta.json()["estado"])