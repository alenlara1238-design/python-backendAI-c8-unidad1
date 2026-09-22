# Guía práctica — Conectar FastAPI con PostgreSQL

# 1. Preparar el proyecto

Partimos de un proyecto FastAPI.

La estructura inicial será:

```text
products-api/
│
├── app/
│   └── main.py
│
└── .venv/
```

Abre la terminal en la carpeta raíz del proyecto.

Por ejemplo:

```text
products-api/
```

---

# 2. Crear el entorno virtual

Ejecuta:

```powershell
python -m venv .venv
```

Este comando crea un entorno virtual llamado:

```text
.venv
```

La estructura ahora será:

```text
products-api/
│
├── app/
│   └── main.py
│
└── .venv/
```

### Comprueba

Verifica que dentro del proyecto apareció la carpeta:

```text
.venv
```

Si apareció, continúa.

---

# 3. Activar el entorno virtual

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si se activó correctamente, deberías observar algo parecido a:

```text
(.venv) PS C:\...\products-api>
```

El indicador:

```text
(.venv)
```

significa que estamos trabajando dentro del entorno virtual.

---

## Si PowerShell bloquea la activación

Si aparece un mensaje relacionado con la ejecución de scripts, ejecuta:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Después intenta nuevamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

# 4. Instalar las dependencias

Con `.venv` activado, ejecuta:

```powershell
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

Estamos instalando cuatro herramientas:

| Paquete           | Función                                            |
| ----------------- | -------------------------------------------------- |
| `fastapi`         | Crear nuestra API                                  |
| `uvicorn`         | Ejecutar FastAPI                                   |
| `sqlalchemy`      | Trabajar con bases de datos desde Python           |
| `psycopg2-binary` | Permitir la comunicación entre Python y PostgreSQL |

### Comprueba

Puedes verificar que SQLAlchemy quedó instalado con:

```powershell
pip show sqlalchemy
```

Y el driver:

```powershell
pip show psycopg2-binary
```

Si aparecen sus respectivos datos de instalación, podemos continuar.

---

# 5. Verificar PostgreSQL

Antes de conectar Python con PostgreSQL necesitamos tener un servidor PostgreSQL instalado y funcionando.

Abre:

**pgAdmin**

Localiza tu servidor PostgreSQL.

Debes poder acceder a él utilizando tu usuario y contraseña.

---

# 6. Crear nuestra base de datos

En pgAdmin:

1. Localiza tu servidor PostgreSQL.
2. Busca **Databases**.
3. Clic derecho sobre **Databases**.
4. Selecciona:

```text
Create → Database
```

5. En el nombre escribe:

```text
products_db
```

6. Guarda.

La estructura debería quedar aproximadamente así:

```text
PostgreSQL
│
└── Databases
    │
    └── products_db
```

> En esta etapa no necesitamos crear ninguna tabla.

---

# 7. Identificar los datos necesarios para la conexión

Para que Python pueda conectarse a PostgreSQL necesitamos conocer:

```text
usuario
contraseña
servidor
puerto
base de datos
```

Una conexión típica tiene esta estructura:

```text
postgresql://usuario:contraseña@servidor:puerto/base_de_datos
```

Por ejemplo:

```text
postgresql://postgres:123456@localhost:5432/products_db
```

En este ejemplo:

```text
postgresql://
│
├── postgres       → usuario
├── 123456         → contraseña
├── localhost      → servidor
├── 5432           → puerto
└── products_db    → base de datos
```

### Importante

No copies literalmente:

```text
123456
```

Debes utilizar **la contraseña que configuraste para tu usuario de PostgreSQL**.

El puerto habitual de PostgreSQL es:

```text
5432
```

salvo que durante la instalación hayas configurado otro.

---

# 8. Crear `database.py`

Dentro de:

```text
app/
```

crea un nuevo archivo:

```text
database.py
```

Ahora tenemos:

```text
products-api/
│
├── app/
│   ├── main.py
│   └── database.py
│
└── .venv/
```

---

# 9. Importar `create_engine`

En `database.py` escribe:

```python
from sqlalchemy import create_engine
```

`create_engine` será la herramienta que utilizaremos para configurar la comunicación con PostgreSQL.

---

# 10. Crear la URL de conexión

Debajo del import escribe:

```python
DATABASE_URL = "postgresql://postgres:TU_PASSWORD@localhost:5432/products_db"
```

Reemplaza:

```text
TU_PASSWORD
```

por la contraseña real de tu usuario de PostgreSQL.

Por ejemplo:

```python
DATABASE_URL = "postgresql://postgres:mi_clave@localhost:5432/products_db"
```

> Para esta práctica utilizaremos la contraseña directamente en el código únicamente para concentrarnos en comprender la conexión. Más adelante aprenderemos a proteger estos datos mediante variables de entorno.

---

# 11. Crear el `Engine`

Debajo de `DATABASE_URL` escribe:

```python
engine = create_engine(DATABASE_URL)
```

Nuestro archivo `database.py` queda:

```python
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:TU_PASSWORD@localhost:5432/products_db"

engine = create_engine(DATABASE_URL)
```

---

# 12. ¿Qué acabamos de hacer?

Todavía **no hemos realizado una consulta**.

Tampoco hemos creado una tabla.

Solamente hemos configurado un `Engine`.

Podemos representarlo así:

```text
database.py
     │
     │ DATABASE_URL
     ↓
create_engine()
     │
     ↓
   Engine
     │
     ↓
PostgreSQL
```

El `Engine` conoce la información necesaria para comunicarse con PostgreSQL.

---

# 13. Preparar `main.py`

Ahora vamos a crear una ruta que nos permita comprobar la conexión.

Abre:

```text
app/main.py
```

Si no tienes contenido todavía, utiliza:

```python
from fastapi import FastAPI

app = FastAPI()
```

---

# 14. Importar el `Engine`

Agrega:

```python
from app.database import engine
```

El archivo queda:

```python
from fastapi import FastAPI

from app.database import engine

app = FastAPI()
```

Ahora `main.py` puede acceder al `Engine` que configuramos en `database.py`.

---

# 15. Importar `text`

También necesitamos importar `text` desde SQLAlchemy:

```python
from sqlalchemy import text
```

El archivo queda:

```python
from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI()
```

---

# 16. Crear la ruta de prueba

Ahora agregaremos nuestra primera ruta para comprobar la conexión.

Debajo de:

```python
app = FastAPI()
```

escribe:

```python
@app.get("/test-db")
def test_database():

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {
        "database": result.scalar()
    }
```

El archivo completo debe quedar:

```python
from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI()


@app.get("/test-db")
def test_database():

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {
        "database": result.scalar()
    }
```

---

# 17. ¿Qué hace esta ruta?

Cuando alguien solicita:

```text
GET /test-db
```

FastAPI ejecuta:

```python
def test_database():
```

Después:

```python
with engine.connect() as connection:
```

utiliza el `Engine` para establecer una conexión con PostgreSQL.

Luego:

```python
result = connection.execute(text("SELECT 1"))
```

envía a PostgreSQL:

```sql
SELECT 1;
```

PostgreSQL responde:

```text
1
```

Finalmente:

```python
result.scalar()
```

obtiene ese valor.

Por eso nuestra API devuelve:

```json
{
  "database": 1
}
```

---

# 18. Ejecutar FastAPI

Desde la carpeta raíz:

```text
products-api/
```

ejecuta:

```powershell
uvicorn app.main:app --reload
```

Si todo está correctamente configurado, Uvicorn mostrará que el servidor está ejecutándose.

---

# 19. Abrir Swagger

En el navegador abre:

```text
http://127.0.0.1:8000/docs
```

Deberías encontrar la ruta:

```text
GET /test-db
```

---

# 20. Probar la conexión

En Swagger:

1. Busca:

```text
GET /test-db
```

2. Haz clic en **Try it out**.
3. Haz clic en **Execute**.

Si la conexión funciona, la respuesta debe ser:

```json
{
  "database": 1
}
```

---

# 21. ¿Qué acabamos de comprobar?

La aplicación todavía **no está trabajando con productos almacenados en PostgreSQL**.

Lo único que hemos demostrado es que:

> **FastAPI puede comunicarse correctamente con PostgreSQL utilizando SQLAlchemy.**

---

# 22. Comprobación final

Antes de terminar, verifica que puedes responder estas preguntas.

### Pregunta 1

¿Qué herramienta permite trabajar con PostgreSQL desde Python?

```text
____________________________
```

### Pregunta 2

¿Qué componente de SQLAlchemy configuramos con `create_engine()`?

```text
____________________________
```

### Pregunta 3

¿Dónde configuramos la información de conexión?

```text
____________________________
```

### Pregunta 4

¿Qué ruta utilizamos para comprobar la conexión?

```text
____________________________
```

### Pregunta 5

¿Qué consulta SQL utilizamos para realizar la prueba?

```text
____________________________
```

### Pregunta 6

¿Qué respuesta esperamos recibir?

```json
{
    "database": ?
}
```

---

# 23. Estado del proyecto

Al terminar esta práctica, la estructura debe ser:

```text
products-api/
│
├── app/
│   ├── main.py
│   └── database.py
│
└── .venv/
```

### `database.py`

```python
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:TU_PASSWORD@localhost:5432/products_db"

engine = create_engine(DATABASE_URL)
```

### `main.py`

```python
from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI()


@app.get("/test-db")
def test_database():

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {
        "database": result.scalar()
    }
```
