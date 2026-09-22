## Pasos rápidos para activar el entorno virtual en Windows

1. **Abre la consola y navega hasta la carpeta de tu proyecto:**

   ```cmd
   cd ruta\de\tu\proyecto
   ```

2. **Ejecuta el comando de activación:**
   ```cmd
   .\venv\Scripts\Activate.ps1
   ```

Sabrás que está activado porque verás el nombre del entorno entre paréntesis al inicio de la línea de comandos, por ejemplo: `(venv) C:\tu\proyecto>`.

---

### Comandos útiles

- **Para desactivarlo:** ejecuta simplemente `deactivate`.
- **Si usas PowerShell (en lugar de CMD):** el comando es `.\venv\Scripts\Activate.ps1`.

# Comandos — FastAPI + PostgreSQL + SQLAlchemy

## 1. Instalar SQLAlchemy y el driver de PostgreSQL

Comando para activar el entonrno virtual (Windows):

```powershell
pip install sqlalchemy psycopg2-binary
```

Enlace de descarga de postgreSQL: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

---

## 2. Ejecutar FastAPI

Desde la carpeta raíz del proyecto:

```powershell
uvicorn nombre_de_archivo_principal:app --reload
```

---

## 3. Abrir Swagger

En el navegador:

```text
http://127.0.0.1:8000/docs
```

---

## 4. Probar la conexión con PostgreSQL

Desde Swagger:

```text
GET /test-db
```

La ruta ejecuta internamente:

```sql
SELECT 1;
```

Respuesta esperada:

```json
{
  "database": 1
}
```

---

## 5. Crear un producto directamente en PostgreSQL

Desde el **Query Tool de pgAdmin**, conectado a `products_db`:

```sql
INSERT INTO products (name, price)
VALUES ('Laptop', 2500);
```

---

## 6. Consultar los productos mediante SQLAlchemy ORM

Desde Swagger:

```text
GET /products-db
```

La consulta ORM utilizada en Python es:

```python
select(Product)
```

Y para obtener todos los resultados:

```python
db.scalars(select(Product)).all()
```

---

## 7. Detener FastAPI

En la terminal donde está ejecutándose Uvicorn:

```text
Ctrl + C
```
