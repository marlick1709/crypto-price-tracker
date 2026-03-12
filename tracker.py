import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
data = requests.get(url).json()

print("Bitcoin price:", data["bitcoin"]["usd"])
print("Ethereum price:", data["ethereum"]["usd"])
