# Pruebas API 📦

Repositorio de ejemplo que alberga varios proyectos web construidos con Python, incluyendo implementaciones en **web.py**, **Flask** y **FastAPI**. Cada uno expone una API REST acompañado de un frontend simple en **HTML**, **CSS** y **JavaScript**.

---

## 📝 Descripción

Este workspace sirve como laboratorio didáctico para aprender a diseñar APIs y aplicaciones web ligeras:

- Endpoints CRUD para recursos (e.g. “cats”).
- Backends en web.py, Flask y FastAPI.
- Plantillas y páginas estáticas que consumen la API con JavaScript.

Las versiones se organizan en carpetas separadas (`CatApi_v2`, `CatApi_v3`, etc.) y se emplean distintos frameworks para comparar estilos de desarrollo.

## 🛠️ Tecnologías

| Capa | Herramientas |
| --- | --- |
| Backend | Python 3.x, web.py, Flask, FastAPI |
| Frontend | HTML5, CSS3, JavaScript (vanilla) |
| Base de datos | MySQL (Supabase) |
| Gestión de dependencias | `requirements.txt` |

## ⚙️ Instalación

1. Clona el repositorio y accede al directorio:
   ```bash
   git clone https://github.com/CristianJavierRG/pruebas_api.git
   cd pruebas_api
   ```

2. Configura un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\\Scripts\\activate   # Windows
   ```

3. Instala dependencias generales:
   ```bash
   pip install -r requirements.txt
   ```

4. Define variables de entorno según la aplicación que ejecutes (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, etc.).

5. Ejecuta el servidor deseado:
   - **web.py:** `python api/app.py` o `python CatApi_v2/app.py`
   - **Flask:** `python path/to/flask_app.py`
   - **FastAPI:** `uvicorn path.to.module:app --reload`

6. Visita el servicio en el navegador (`http://localhost:8080` para web.py, `http://localhost:8000` para FastAPI, etc.).

## 🚀 Endpoints

Los endpoints varían ligeramente entre versiones, pero siguen el patrón REST:

```http
GET    /items
POST   /items
```
Ejemplos concretos (web.py):

- `GET /cats` – lista gatos

Consulta cada carpeta para rutas y modelos específicos.

## 📁 Estructura del proyecto

```

├── CatApi_v3/               # web.py v3
├── pruebas/
│   ├── catapi/              # pruebas varias
│   ├── api/                     # web.py v1
│   ├── CatApi_v2/               # web.py v2
│   ├── CatApi_v3 copy/          # copia de trabajo
│   └── openrouteservice/
├── requirements.txt         # dependencias globales
└── README.md                # documentación general
```

## ✍️ Autor

**Cristian Javier** – desarrollador y educador.

[GitHub](https://github.com/CristianJavierRG)

---