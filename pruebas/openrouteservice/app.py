import requests

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

response = requests.get(url, headers=headers, params=params)

print(f"STATUS_CODE: {response.status_code}")

print(response.status_code, response.reason)

print(response.text)
# Extraer el summary (QL)
"""
data = response.json()
summary = data["features"][0]["properties"]["summary"] 

print("QL (summary):") 
print("Distancia:", summary["distance"], "metros") 
print("Duración:", summary["duration"], "segundos")
"""