# Image Scraper

Aplicación web que permite extraer imágenes de cualquier sitio web y guardarlas como favoritos.

## Características

- Extracción de imágenes desde cualquier URL
- Sistema de autenticación (registro/login)
- Guardar imágenes favoritas
- Ver y gestionar favoritos
- Interfaz moderna con Bulma CSS

## Tecnologías

- Django 6.0
- PostgreSQL
- Bulma CSS
- Python 3.12

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/image-scraper.git
cd image-scraper
```

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install django psycopg2-binary beautifulsoup4 requests
```

4. Configurar PostgreSQL:
```bash
sudo -u postgres psql
CREATE DATABASE scraper_db;
CREATE USER admin WITH PASSWORD 'tu_password';
GRANT ALL PRIVILEGES ON DATABASE scraper_db TO admin;
\q
```

5. Migrar base de datos:
```bash
python manage.py migrate
```

6. Ejecutar servidor:
```bash
python manage.py runserver
```

7. Abrir en el navegador: `http://localhost:8000`

## Uso

1. Registrarse o iniciar sesión
2. Pegar URL de un sitio web
3. Click en "Search" para extraer imágenes
4. Guardar las imágenes que te gusten como favoritas
5. Ver tus favoritos en la página de Favorites

## Deploy

El proyecto está preparado para deploy en Render o Railway con PostgreSQL.

## Autor

Tu nombre - [GitHub](https://github.com/tu-usuario)

## Licencia

MIT
