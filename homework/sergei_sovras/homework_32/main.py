import requests

request = requests.get('https://www.onliner.by/sdapi/pogoda/api/now')
weather = request.json()
print(f"В {weather['city']} сегодня: {weather['temperature']}")
