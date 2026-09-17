# Guía rápida — Verbos HTTP en FastAPI

Hasta ahora hemos trabajado principalmente con:

```text
GET
POST
```

Ahora vamos a conocer otros tres verbos HTTP:

```text
PUT
PATCH
DELETE
```

Para entenderlos, continuaremos trabajando con nuestra API de **productos**.

---

# 1. GET — Consultar

Ya conocemos `GET`.

Su función principal es:

> **Obtener información.**

Por ejemplo:

```python
@app.get("/products")
def get_products():
    return products
```

Podemos consultar todos los productos:

```text
GET /products
```

O consultar uno:

```text
GET /products/2
```

No estamos modificando los datos.

---

# 2. POST — Crear

También conocemos `POST`.

Su función principal es:

> **Crear un nuevo recurso.**

Por ejemplo:

```python
@app.post("/products")
def create_product(product: dict):
    return product
```

Enviamos:

```json
{
    "id": 5,
    "name": "Webcam",
    "price": 300,
    "category": "Periféricos"
}
```

Estamos indicando:

> Quiero crear un nuevo producto.

---

# 3. PUT — Actualizar completamente

`PUT` se utiliza para:

> **Reemplazar o actualizar completamente un recurso existente.**

Imaginemos que tenemos este producto:

```json
{
    "id": 2,
    "name": "Mouse",
    "price": 80,
    "category": "Periféricos"
}
```

Queremos cambiar toda su información.

La ruta podría ser:

```text
PUT /products/2
```

Ejemplo:

```python
@app.put("/products/{product_id}")
def update_product(product_id: int, product: dict):
    return {
        "id": product_id,
        "name": product["name"],
        "price": product["price"],
        "category": product["category"]
    }
```

En Swagger podríamos enviar:

```json
{
    "name": "Mouse Gamer",
    "price": 150,
    "category": "Periféricos"
}
```

La idea sería:

```text
Producto anterior
        ↓
     PUT /products/2
        ↓
Información nueva
        ↓
Producto actualizado
```

## Ejemplo conceptual

Antes:

```json
{
    "id": 2,
    "name": "Mouse",
    "price": 80,
    "category": "Periféricos"
}
```

Después:

```json
{
    "id": 2,
    "name": "Mouse Gamer",
    "price": 150,
    "category": "Periféricos"
}
```

### ¿Cuándo utilizar PUT?

Cuando queremos enviar la **nueva versión completa** del recurso.

---

# 4. PATCH — Actualizar parcialmente

`PATCH` también sirve para actualizar.

Pero existe una diferencia importante:

> **PATCH permite modificar solamente una parte del recurso.**

Supongamos que tenemos:

```json
{
    "id": 2,
    "name": "Mouse",
    "price": 80,
    "category": "Periféricos"
}
```

Solamente queremos cambiar el precio.

No necesitamos enviar nuevamente toda la información.

Utilizamos:

```text
PATCH /products/2
```

Y enviamos:

```json
{
    "price": 100
}
```

Conceptualmente:

```text
Producto
   │
   ├── id: 2
   ├── name: Mouse
   ├── price: 80  ← modificar
   └── category: Periféricos
              │
              ▼
       PATCH /products/2
              │
              ▼
          price: 100
```

Ejemplo sencillo:

```python
@app.patch("/products/{product_id}")
def update_product_price(product_id: int, data: dict):
    return {
        "id": product_id,
        "price": data["price"]
    }
```

Enviamos:

```json
{
    "price": 100
}
```

### ¿Cuándo utilizar PATCH?

Cuando queremos modificar **solamente una parte** de un recurso.

---

# 5. PUT vs PATCH

Esta es una diferencia importante que debemos recordar:

| Verbo    | Función                  |
| -------- | ------------------------ |
| `GET`    | Consultar                |
| `POST`   | Crear                    |
| `PUT`    | Actualizar completamente |
| `PATCH`  | Actualizar parcialmente  |
| `DELETE` | Eliminar                 |

### Ejemplo

Tenemos:

```json
{
    "id": 2,
    "name": "Mouse",
    "price": 80,
    "category": "Periféricos"
}
```

### PUT

Enviamos la nueva información completa:

```json
{
    "name": "Mouse Gamer",
    "price": 150,
    "category": "Periféricos"
}
```

### PATCH

Enviamos solamente lo que queremos cambiar:

```json
{
    "price": 150
}
```

---

# 6. DELETE — Eliminar

`DELETE` se utiliza para:

> **Eliminar un recurso.**

Por ejemplo:

```text
DELETE /products/2
```

Estamos indicando:

> Elimina el producto cuyo ID es 2.

Ejemplo:

```python
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return {
        "message": "Producto eliminado",
        "id": product_id
    }
```

Podemos probarlo desde Swagger:

```text
DELETE /products/2
```

Y obtener:

```json
{
    "message": "Producto eliminado",
    "id": 2
}
```

---

# 7. Los cinco verbos juntos

Podemos pensar en un producto:

```text
Producto
   │
   ├── GET       → consultar
   │
   ├── POST      → crear
   │
   ├── PUT       → actualizar completamente
   │
   ├── PATCH     → actualizar parcialmente
   │
   └── DELETE    → eliminar
```

Por ejemplo:

```text
GET    /products
POST   /products

GET    /products/2
PUT    /products/2
PATCH  /products/2
DELETE /products/2
```

Observa que las rutas pueden ser iguales:

```text
/products/2
```

Lo que cambia es el **verbo HTTP**.

---

# 8. Ejemplo completo

Podemos tener:

```python
from fastapi import FastAPI

app = FastAPI()

products = [
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
    }
]


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "id": product_id
    }


@app.post("/products")
def create_product(product: dict):
    return product


@app.put("/products/{product_id}")
def update_product(product_id: int, product: dict):
    return {
        "id": product_id,
        "product": product
    }


@app.patch("/products/{product_id}")
def partial_update_product(product_id: int, data: dict):
    return {
        "id": product_id,
        "changes": data
    }


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return {
        "message": "Producto eliminado",
        "id": product_id
    }
```

> Este ejemplo se concentra en entender los verbos y las rutas. Todavía no estamos implementando un CRUD completo ni validaciones.

---

# 9. Probar desde Swagger

Ejecuta:

```powershell
uvicorn app.main:app --reload
```

Abre:

```text
http://127.0.0.1:8000/docs
```

Deberías encontrar:

```text
GET
POST
PUT
PATCH
DELETE
```

Prueba cada uno utilizando **Try it out**.

---

# 10. Ejercicio guiado

Utilizando la API de productos que ya construiste:

## Paso 1

Agrega:

```text
PUT /products/{product_id}
```

Debe permitir actualizar completamente un producto.

---

## Paso 2

Agrega:

```text
PATCH /products/{product_id}
```

Debe permitir modificar solamente el precio de un producto.

---

## Paso 3

Agrega:

```text
DELETE /products/{product_id}
```

Debe eliminar un producto.

---

## Paso 4

Prueba todas las rutas desde Swagger.

Debes poder realizar:

```text
GET     → consultar
POST    → crear
PUT     → actualizar completamente
PATCH   → actualizar parcialmente
DELETE  → eliminar
```

---

# 11. Preguntas de comprobación

Antes de terminar, responde:

1. ¿Qué verbo utilizamos para consultar?
2. ¿Qué verbo utilizamos para crear?
3. ¿Qué verbo utilizamos para actualizar completamente?
4. ¿Qué verbo utilizamos para actualizar parcialmente?
5. ¿Qué verbo utilizamos para eliminar?
6. Si solamente quiero cambiar el precio de un producto, ¿utilizaría `PUT` o `PATCH`?
7. Si quiero eliminar `/products/5`, ¿qué verbo utilizaría?
8. ¿Puede existir `/products/5` para diferentes verbos HTTP?

---
