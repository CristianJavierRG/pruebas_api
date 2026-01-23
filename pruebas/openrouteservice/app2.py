import requests
import json

url = "https://api.openrouteservice.org/v2/directions/wheelchair"
api_key = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjIzY2FiYWE5MDIwZjQ3ZTFhODAxYjUxZjA2MzYzOWE1IiwiaCI6Im11cm11cjY0In0="
start = "8.681495,49.41461"
end = "8.687872,49.420318"

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
}

params = {
    "api_key": api_key,
    "start": start,
    "end": end
}

call = requests.get(url, headers=headers, params=params)

data = json.loads(call.text)

print(f"TYPE: {type(call)}")
print(f"STATUS_CODE: {call.status_code}")
print(call.status_code, call.reason)

if call.status_code == 403:
    print("ERROR: API KEY incorrecta")
elif call.status_code == 200:
    print("BIEN: Todo salio OK")

for keys in data:
    print(f"keys: {keys}")

query = data["metadata"]

print("Atribución: ", query["attribution"])
print("Servicio: ", query["service"])
print("Sello de Tiempo: ", query["timestamp"])
print("Consulta: ", query["query"])
