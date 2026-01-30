from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

API_KEY = "live_7NJGZaisRFcQewUy1qnYS779chPlFf5F4XTDLhKKZZ5m2dGeV5VDpr6HsiyOL1RO"
URL = "https://api.thecatapi.com/v1/images/search?has_breeds=1"
GIPHY_API_KEY = "dc6zaTOxFJmzC"

# Cache para almacenar datos de gatos por ID
cat_cache = {}


@app.route("/", methods=["GET", "POST"])
def index():
    images = []
    error = None

    if request.method == "POST":
        limit = request.form.get("limit", 1)

        params = {
            "limit": limit,
            "api_key": API_KEY
        }

        call = requests.get(URL, params=params)
        
        data = json.loads(call.text)
        if call.status_code == 200:
            images = data
            # Almacenar gatos en cache para acceso rápido
            for cat in images:
                cat_cache[cat['id']] = cat
            print(f"TYPE: {type(call)}")
            print(f"STATUS_CODE: {call.status_code}")
            print(data)
        elif call.status_code == 403:
            error = "❌ API KEY incorrecta"
        else:
            error = f"❌ Error {call.status_code}"

    return render_template("index.html", images=images, error=error)


@app.route("/cat/<cat_id>")
def cat_details(cat_id):
    """Mostrar detalles completos del gato"""
    cat = cat_cache.get(cat_id)
    
    if not cat:
        error = "❌ Gato no encontrado"
        return render_template("details.html", cat=None, error=error)
    
    return render_template("details.html", cat=cat)


@app.route("/api/gifs")
def get_gifs():
    """API para obtener GIFs de gatos desde Giphy"""
    limit = request.args.get("limit", 12)
    giphy_url = f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q=cat&limit={limit}&rating=g"
    
    try:
        response = requests.get(giphy_url)
        data = response.json()
        return jsonify(data)
    except:
        return jsonify({"error": "No se pudieron cargar los GIFs"}), 400


if __name__ == "__main__":
    app.run(debug=True)
