import requests 
import json
import webbrowser

call = requests.get('https://api.mridul.tech/api/breaking-bad/characters')

data = json.loads(call.text)
print(data)

print(f"TYPE: {type(call)}")
print(f"STATUS_CODE: {call.status_code}")

print(call.status_code, call.reason)

if call.status_code == 200:
    imagenes = [p["image_url"] for p in data["data"]]
    for img in imagenes:
        webbrowser.open(img)

elif call.status_code == 403:
    print("ERROR: API KEY incorrecta")