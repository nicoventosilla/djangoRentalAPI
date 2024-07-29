# djangoRentalAPI

djangoRentalAPI es una API RESTful para gestionar ofertas de alquiler de propiedades. Está construida con Django y Django REST Framework.

## Requisitos

- Python 3.8+
- Django 5.0.7
- Django REST Framework
- PostgreSQL

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/djangoRentalAPI.git
    cd djangoRentalAPI
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno en un archivo `.env`:
    ```env
    SECRET_KEY=tu_secreto
    DEBUG=True
    DB_NAME=nombre_de_tu_base_de_datos
    DB_USERNAME=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_HOST=localhost
    DB_PORT=5432
    ```

5. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

6. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Endpoints

- `GET /offers/` - Lista todas las ofertas
- `POST /offers/` - Crea una nueva oferta
- `GET /offers/{id}/` - Detalles de una oferta
- `PUT /offers/{id}/` - Actualiza una oferta
- `DELETE /offers/{id}/` - Elimina una oferta
- `GET /users/` - Lista todos los usuarios
- `GET /users/{id}/` - Detalles de un usuario

## Autenticación

La API utiliza autenticación básica proporcionada por Django REST Framework. Para acceder a los endpoints protegidos, debes autenticarte con un nombre de usuario y contraseña.

## Agradecimientos

Este proyecto fue desarrollado siguiendo el tutorial [Building APIs With Django REST Framework](https://blog.jetbrains.com/pycharm/2023/09/building-apis-with-django-rest-framework) por Denis Mashutin. Agradezco a Denis Mashutin por su excelente guía.
