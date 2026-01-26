import requests 
# Tu clave de API (reemplaza REPLACE_ME por la real) 
api_key = "TU_API_KEY_AQUI" 
# Construir la URL con parámetros 
url = f"https://api.thecatapi.com/v1/images/search?limit=10&api_key={api_key}" 
# Hacer la petición 
respuesta = requests.get(url) 
# Convertir a JSON 
imagenes = respuesta.json() 
# Mostrar las URLs de las imágenes 
for i, img in enumerate(imagenes, start=1): 
    print(f"Imagen {i}: {img['url']}")