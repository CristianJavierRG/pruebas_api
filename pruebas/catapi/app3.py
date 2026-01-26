import requests
import json
import webbrowser

limit = input("¿Cuantas Imagenes Quieres?")

api_key = "live_7NJGZaisRFcQewUy1qnYS779chPlFf5F4XTDLhKKZZ5m2dGeV5VDpr6HsiyOL1RO"
url = f"https://api.thecatapi.com/v1/images/search?limit={limit}"

params = {
    "api_key": api_key,
}

call = requests.get(url,params=params)

data = json.loads(call.text)

print(f"TYPE: {type(call)}")
print(f"STATUS_CODE: {call.status_code}")

print(call.status_code, call.reason)

if call.status_code == 200:
    for img in data: 
        webbrowser.open(img['url'])

elif call.status_code == 403:
    print("ERROR: API KEY incorrecta")
