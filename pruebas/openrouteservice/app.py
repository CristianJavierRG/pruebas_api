import requests

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
}
call = requests.get('https://api.openrouteservice.org/v2/directions/wheelchair?api_key=your-api-key&start=8.681495,49.41461&end=8.687872,49.420318', headers=headers)

print(call.status_code, call.reason)
print(call.text)