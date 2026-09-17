# Comandos esenciales — FastAPI

## 0. Enlace de instalación de Cursor AI

https://cursor.com/es/download

## 1. Crear un entorno virtual

Dentro de la carpeta del proyecto:

```powershell
python -m venv .venv
```

---

## 2. Activar el entorno virtual

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si se activó correctamente, aparecerá:

```text
(.venv) PS C:\...\proyecto>
```

---

## 3. Si PowerShell bloquea la activación

Ejecutar:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Después volver a ejecutar:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 4. Desactivar el entorno virtual

```powershell
deactivate
```

---

## 5. Instalar FastAPI y Uvicorn

Con el entorno virtual activado:

```powershell
pip install fastapi uvicorn
```

---

## 6. Ejecutar FastAPI con Uvicorn

Si tenemos:

```text
app/
└── main.py
```

y dentro de `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()
```

ejecutamos:

```powershell
uvicorn app.main:app
```

---

## 7. Ejecutar con recarga automática

Durante el desarrollo utilizaremos:

```powershell
uvicorn app.main:app --reload
```

La opción `--reload` permite que el servidor se reinicie automáticamente cuando detecta cambios en el código.

---

## 8. Especificar host y puerto

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000
```

---

## 9. Cambiar el puerto

Por ejemplo, para utilizar el puerto `8001`:

```powershell
uvicorn app.main:app --reload --port 8001
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8001
```

---

## 10. Detener el servidor

En la terminal donde está ejecutándose Uvicorn:

```text
Ctrl + C
```

---

## 11. Abrir la API en el navegador

Si estamos utilizando el puerto `8000`:

```text
http://127.0.0.1:8000
```

---

## 12. Abrir Swagger

FastAPI genera automáticamente una interfaz para probar y documentar la API.

Abrir en el navegador:

```text
http://127.0.0.1:8000/docs
```

Desde Swagger podemos:

- Visualizar las rutas.
- Consultar los métodos HTTP.
- Ejecutar peticiones.
- Enviar parámetros.
- Enviar datos JSON.
- Visualizar las respuestas.
