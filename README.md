
# Proyecto Registro de Usuarios – Backend

Este es el backend de la aplicación de registro de usuarios. Desarrollado con Flask, se encarga de manejar las rutas de registro, obtención, edición y eliminación de usuarios, y de interactuar con la base de datos.

## Tecnologías usadas

- Python 
- Flask
- SQLAlchemy
- Flask-CORS
- Werkzeug (para hashear contraseñas)
- SQLite (base de datos local)

## Archivos principales

- `app.py`: configuración general de Flask y la base de datos.
- `models.py`: definición del modelo de usuario.
- `routes.py`: rutas para registrar, editar, obtener y eliminar usuarios.

## Seguridad

- Las contraseñas se encriptan usando `generate_password_hash()`.
- Para editar un usuario se requiere verificar la contraseña enviada por el cliente.

## Conexión con frontend

El backend responde a peticiones desde el frontend usando rutas RESTful como:

- `POST /register`
- `GET /users`
- `PUT /users/<id>`
- `DELETE /users/<id>`

