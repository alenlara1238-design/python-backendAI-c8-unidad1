# Ejercicios guiados — FastAPI

## Objetivo

En estos ejercicios practicarás la construcción de APIs REST utilizando **FastAPI**.

La estructura inicial será un solo entorno virtal y los archivos de código estarán dentro de la carpeta `app/`.:

```text
proyecto/
│
├── .venv/
└── app/
    └── ejercicio1.py
    └── ejercicio2.py
    └── ejercicion.py
```

---

# Ejercicio 1 — API de Películas

## Contexto

Una plataforma de entretenimiento necesita una API sencilla para consultar y registrar películas.

Debes construir una API que permita consultar las películas disponibles y registrar nuevas películas.

## Endpoints

Implementa las siguientes rutas:

```text
GET  /movies
GET  /movies/{movie_id}
POST /movies
```

Todas deben estar en:

```text
app/main.py
```

## Datos iniciales

La API debe comenzar con estas películas, por tanto, debes crear una lista de diccionarios en `ejercicio1.py` con la siguiente información:

```json
[
  {
    "id": 1,
    "title": "Interstellar",
    "year": 2014
  },
  {
    "id": 2,
    "title": "The Matrix",
    "year": 1999
  },
  {
    "id": 3,
    "title": "Inception",
    "year": 2010
  }
]
```

## Requerimientos

### `GET /movies`

Debe devolver todas las películas.

### `GET /movies/{movie_id}`

Debe recibir el identificador de una película mediante la URL.

Ejemplo:

```text
GET /movies/2
```

Debe devolver la película correspondiente.

### `POST /movies`

Debe recibir una nueva película y devolver una respuesta indicando que fue recibida.

Ejemplo de información enviada:

```json
{
  "id": 4,
  "title": "Avatar",
  "year": 2009
}
```

## Comprobación

Abre Swagger:

```text
http://127.0.0.1:8000/docs
```

Prueba los tres endpoints.

## Preguntas de reflexión

1. ¿Qué representa `/movies`?
2. ¿Qué representa `{movie_id}`?
3. ¿Qué diferencia existe entre `GET` y `POST`?

---

# Ejercicio 2 — API de Libros

## Contexto

Una biblioteca quiere disponer de una API para consultar su catálogo de libros.

Cada libro contiene:

```text
id
title
author
year
```

## Endpoints

Implementa:

```text
GET  /books
GET  /books/{book_id}
POST /books
```

Todas las rutas deben estar en:

```text
app/main.py
```

## Datos iniciales

Utiliza como mínimo estos libros:

```json
[
  {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "year": 2008
  },
  {
    "id": 2,
    "title": "The Pragmatic Programmer",
    "author": "Andrew Hunt",
    "year": 1999
  },
  {
    "id": 3,
    "title": "Design Patterns",
    "author": "Erich Gamma",
    "year": 1994
  }
]
```

## Requerimientos

### `GET /books`

Debe devolver todos los libros.

### `GET /books/{book_id}`

Debe permitir consultar un libro específico.

Ejemplo:

```text
GET /books/1
```

### `POST /books`

Debe recibir la información de un nuevo libro.

Ejemplo:

```json
{
  "id": 4,
  "title": "Refactoring",
  "author": "Martin Fowler",
  "year": 1999
}
```

## Reto adicional

Crea una ruta:

```text
GET /books/author/{author_name}
```

que permita consultar los libros de un autor determinado.

Por ejemplo:

```text
GET /books/author/Robert C. Martin
```

## Preguntas

Antes de implementar el reto, responde:

1. ¿Qué parte de la URL representa el parámetro?
2. ¿Qué nombre tendrá el parámetro en la función?
3. ¿Qué método HTTP utilizarás?
4. ¿Qué deberá devolver la función?

---

# Ejercicio 3 — API de Cursos

## Contexto

Una plataforma educativa necesita una API para consultar los cursos disponibles.

Cada curso contiene:

```text
id
name
teacher
duration
```

Donde `duration` representa la duración del curso en horas.

## Endpoints obligatorios

```text
GET  /courses
GET  /courses/{course_id}
POST /courses
```

## Datos iniciales

```json
[
  {
    "id": 1,
    "name": "Python desde Cero",
    "teacher": "Laura",
    "duration": 20
  },
  {
    "id": 2,
    "name": "Java Backend",
    "teacher": "Carlos",
    "duration": 30
  },
  {
    "id": 3,
    "name": "JavaScript Moderno",
    "teacher": "Andrés",
    "duration": 25
  }
]
```

## Requerimientos

### `GET /courses`

Debe devolver todos los cursos.

### `GET /courses/{course_id}`

Ejemplo:

```text
GET /courses/2
```

Debe devolver:

```json
{
  "id": 2,
  "name": "Java Backend",
  "teacher": "Carlos",
  "duration": 30
}
```

### `POST /courses`

Debe recibir un nuevo curso.

Ejemplo:

```json
{
  "id": 4,
  "name": "FastAPI",
  "teacher": "Ana",
  "duration": 15
}
```

## Reto adicional

Agrega:

```text
GET /courses/teacher/{teacher_name}
```

Debe devolver los cursos impartidos por un determinado profesor.

## Comprobación

Utiliza Swagger para probar:

```text
GET /courses
GET /courses/{course_id}
POST /courses
GET /courses/teacher/{teacher_name}
```

## Preguntas de reflexión

1. ¿Qué ruta permite obtener todos los cursos?
2. ¿Qué ruta permite obtener un único curso?
3. ¿Qué información se encuentra en la URL?
4. ¿Qué información se envía en el `POST`?
5. ¿Qué diferencia existe entre un parámetro de ruta y el cuerpo de una petición?

---

# Ejercicio 4 — API de Productos

## Contexto

Una tienda en línea necesita una API para consultar sus productos.

Cada producto contiene:

```text
id
name
price
category
```

## Endpoints

Implementa:

```text
GET  /products
GET  /products/{product_id}
POST /products
```

## Datos iniciales

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 2500,
    "category": "Computadores"
  },
  {
    "id": 2,
    "name": "Mouse",
    "price": 80,
    "category": "Periféricos"
  },
  {
    "id": 3,
    "name": "Teclado",
    "price": 150,
    "category": "Periféricos"
  },
  {
    "id": 4,
    "name": "Monitor",
    "price": 900,
    "category": "Monitores"
  }
]
```

## Requerimientos

### `GET /products`

Devuelve todos los productos.

### `GET /products/{product_id}`

Permite consultar un producto específico.

Ejemplo:

```text
GET /products/3
```

### `POST /products`

Recibe un nuevo producto.

Ejemplo:

```json
{
  "id": 5,
  "name": "Webcam",
  "price": 300,
  "category": "Periféricos"
}
```

## Reto adicional

Crea:

```text
GET /products/category/{category_name}
```

Por ejemplo:

```text
GET /products/category/Periféricos
```

Debe devolver únicamente los productos pertenecientes a esa categoría.

## Preguntas

Antes de programar el reto:

1. ¿Qué información debe recibir la función?
2. ¿Dónde estará esa información?
3. ¿Qué debe recorrer la función?
4. ¿Qué condición debe comprobar?
5. ¿Qué estructura de datos debería devolver?

---

# Ejercicio 5 — API de Eventos

## Contexto

Una plataforma de eventos necesita una API para consultar los eventos disponibles.

Cada evento contiene:

```text
id
name
city
date
```

## Endpoints obligatorios

Implementa:

```text
GET  /events
GET  /events/{event_id}
POST /events
```

## Datos iniciales

```json
[
  {
    "id": 1,
    "name": "Conferencia de Python",
    "city": "Bogotá",
    "date": "2026-10-15"
  },
  {
    "id": 2,
    "name": "Java Backend Summit",
    "city": "Medellín",
    "date": "2026-11-05"
  },
  {
    "id": 3,
    "name": "JavaScript Conference",
    "city": "Cali",
    "date": "2026-11-20"
  }
]
```

## Requerimientos

### `GET /events`

Devuelve todos los eventos.

### `GET /events/{event_id}`

Permite consultar un evento específico.

Ejemplo:

```text
GET /events/2
```

### `POST /events`

Debe permitir enviar un nuevo evento.

Ejemplo:

```json
{
  "id": 4,
  "name": "FastAPI Workshop",
  "city": "Cartagena",
  "date": "2026-12-10"
}
```

---

## Reto 1 — Eventos por ciudad

Crea:

```text
GET /events/city/{city_name}
```

Ejemplo:

```text
GET /events/city/Bogotá
```

Debe devolver únicamente los eventos de esa ciudad.

---

## Reto 2 — Diseña tu propia ruta

Crea una nueva ruta relacionada con los eventos.

Antes de escribir código, define:

```text
Ruta:
Método HTTP:
Parámetro:
Información que recibe:
Información que devuelve:
```

Después implementa la ruta y compruébala desde Swagger.

---

# Desafío final — Construye tu propia API

Selecciona uno de los siguientes dominios:

```text
1. Series
2. Videojuegos
3. Restaurantes
4. Empleados
5. Vehículos
```

Construye una API que tenga como mínimo:

```text
GET  /recursos
GET  /recursos/{id}
POST /recursos
```

## Requisitos

La API debe:

- Utilizar FastAPI.
- Utilizar una lista para almacenar los datos.
- Devolver respuestas JSON.
- Utilizar al menos un parámetro de ruta.
- Tener una ruta `POST`.
- Poder probarse completamente desde Swagger.

## Ejemplo

Si seleccionas videojuegos:

```text
GET  /games
GET  /games/{game_id}
POST /games
```

Puedes definir cada videojuego con:

```text
id
title
genre
year
```

Los datos y nombres son responsabilidad del estudiante.

---

# Checklist final

Antes de considerar terminado el ejercicio:

- [ ] El entorno virtual está funcionando.
- [ ] FastAPI está instalado.
- [ ] Uvicorn está instalado.
- [ ] La aplicación inicia correctamente.
- [ ] Existe `app/main.py`.
- [ ] Las rutas están definidas en `main.py`.
- [ ] Se utiliza al menos una ruta `GET`.
- [ ] Se utiliza una ruta con parámetro.
- [ ] Se utiliza una ruta `POST`.
- [ ] Las respuestas son JSON.
- [ ] Swagger funciona.
- [ ] Todas las rutas pueden probarse desde `/docs`.
- [ ] Los datos se mantienen temporalmente en memoria.

---

# Preguntas de cierre

Responde con tus propias palabras:

1. ¿Qué es FastAPI?
2. ¿Qué función cumple Uvicorn?
3. ¿Qué es una ruta?
4. ¿Qué diferencia existe entre `GET` y `POST`?
5. ¿Qué es un parámetro de ruta?
6. ¿Dónde se encuentra el parámetro `{product_id}`?
