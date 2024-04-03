
# MANSTYLE API

<p align="justify">

Description
La API MANSTYLE es una API sencilla y fácil de usar para gestionar carteras. Proporciona puntos finales para crear, leer, actualizar y eliminar billeteras. La API utiliza tokens JWT para autenticación y autorización.

</p>

<p align="justify">

## Tabla de contenido
- **Instalación**
Usage
Endpoints
GET /
GET /wallets
GET /wallet/{id}
GET /wallets?category={category}
POST /wallets
PUT /wallets/{id}
DELETE /wallets/{id}
POST /login
License

</p>


## Installation

<p align="justify">
Para instalar y ejecutar la API, necesita tener Python y pip instalados en su sistema. Sigue estos pasos:

- **Clonar el repositorio:**

1. clon de git https://github.com/your-username/manstyle-api.git

2. Navegue a la carpeta del proyecto:
cd manstyle-api

3. Cree un entorno virtual (opcional pero recomendado):

python3 -m venv venv
fuente venv/bin/activate (para Linux/macOS)
venv\Scripts\activate (para Windows)

4. Instale los paquetes necesarios:
instalación de pip -r requisitos.txt

5. Ejecute la aplicación:
aplicación python.py

6. La solicitud estará disponible en
http://127.0.0.1:8000/.

</p>

## Uso

<p align="justify">

La API proporciona varios puntos finales para administrar billeteras. Debe generar un token JWT para acceder a los puntos finales. Utilice el punto final /login para generar un token.

Aquí hay un ejemplo de cómo usar la API con curl:

Inicie sesión para obtener un token:
curl -X POST "http://127.0.0.1:8000/login" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"email\":\"admin@gmail.com\",\"password\":\"admin\"}"

2. Guarde el token:
TOKEN=<your-token-here>

3. Utilice el token para acceder a los puntos finales:
curl -X GET "http://127.0.0.1:8000/wallets" -H "accept: application/json" -H "Authorization: Bearer ${TOKEN}"

Endpoints
GET /
Devuelve un mensaje de bienvenida.

GET /wallets
Devuelve una lista de todas las carteras.

GET /wallet/{id}
Devuelve una billetera específica por ID.

GET /wallets?category={category}
Devuelve una lista de billeteras que pertenecen a una categoría específica.

POST /wallets
Creas  una nueva billetera.

PUT /wallets/{id}
Actualiza una billetera existente.

DELETE /wallets/{id}
Eliminar billeteras

POST /login
Genera un token JWT para autenticación.
</p>