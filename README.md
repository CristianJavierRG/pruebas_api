# Pruebas API 📦

Proyecto de ejemplo que demuestra el uso de **web.py** con una base de datos **MySQL** hospedada en **Supabase**, y front-end sencillo en HTML. El propósito es servir como referencia para el desarrollo de APIs REST ligeras con Python.

---

## 📝 Descripción

Esta aplicación ofrece varias versiones (`CatApi_v2`, `CatApi_v3`, etc.) que ilustran cómo construir y estructurar endpoints REST utilizando web.py. La base de datos se gestiona a través de Supabase/MySQL y la interfaz de usuario se entrega mediante plantillas HTML.

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.x
- **Framework:** [web.py](https://webpy.org/)
- **Base de datos:** MySQL vía [Supabase](https://supabase.com/)
- **Frontend:** HTML/CSS con plantillas simples
- **Dependencias:** Listadas en `requirements.txt`

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/CristianJavierRG/pruebas_api.git
   cd pruebas_api
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno para la conexión a Supabase/MySQL (ej. `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`).

5. Inicia la aplicación:
   ```bash
   python api/app.py
   ```

6. Accede al servicio en `http://localhost:8080/` o según el puerto configurado.

## 🚀 Endpoints

El proyecto incluye diferentes módulos (`api/app.py`, `CatApi_v2/app.py`, `CatApi_v3/app.py`, etc.), cada uno con sus propios endpoints. Algunos ejemplos comunes:

- `GET /cats` – Lista todos los gatos.
- `GET /cats/<id>` – Detalle de un gato.

> **Nota:** Revisa el código de cada versión para ver la implementación y rutas exactas.

## 📁 Estructura del proyecto

```
├── CatApi_v3/
│   └── app.py                
├── pruebas/                  
│   ├── catapi/
│   ├── api/
│   ├── CatApi_v2/
│   └── openrouteservice/
├── requirements.txt
└── README.md
```

## ✍️ Autor

**Cristian Javier**

Puedes contactarme a través de [mi perfil en GitHub](https://github.com/CristianJavierRG).

---