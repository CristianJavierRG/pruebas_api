from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

API_KEY = "live_7NJGZaisRFcQewUy1qnYS779chPlFf5F4XTDLhKKZZ5m2dGeV5VDpr6HsiyOL1RO"
URL = "https://api.thecatapi.com/v1/images/search?"

@app.route("/", methods=["GET", "POST"])
def index():
    images = []
    error = None

    mime = request.values.get("mime_types", "jpg,png")
    limit = request.values.get("limit")
    has_breeds = request.values.get("has_breeds", "0")

    if limit:
        params = {
            "limit": limit,
            "mime_types": mime,
            "api_key": API_KEY
        }

        if has_breeds == '1':
            params["has_breeds"] = 1

        call = requests.get(URL, params=params)
        
        data = json.loads(call.text)
        if call.status_code == 200:
            images = data
            print(f"TYPE: {type(call)}")
            print(f"STATUS_CODE: {call.status_code}")
        elif call.status_code == 403:
            error = "❌ API KEY incorrecta"
        else:
            error = f"❌ Error {call.status_code}"

    return render_template("index.html", images=images, error=error, mime=mime)

if __name__ == "__main__":
    app.run(debug=True)
