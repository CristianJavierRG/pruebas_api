import web
import requests

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        # Términos de Fallout que queremos mostrar
        titles = [
            "Vault_Boy",
            "Power_Armor",
            "Pip-Boy",
            "Brotherhood_of_Steel",
            "Nuka-Cola"
        ]

        personajes = []

        for t in titles:
            url = "https://fallout.fandom.com/api.php"
            params = {
                "action": "query",
                "format": "json",
                "prop": "pageimages|extracts",
                "piprop": "thumbnail",
                "pithumbsize": 300,
                "exintro": True,
                "explaintext": True,
                "titles": t
            }

            res = requests.get(url, params=params).json()
            pages = res["query"]["pages"]

            for _, page in pages.items():
                personajes.append({
                    "title": page.get("title"),
                    "img": page.get("thumbnail", {}).get("source"),
                    "extract": page.get("extract")
                })

        return render.index(personajes)

if __name__ == "__main__":
    app.run()
