from fastapi import FastAPI

app = FastAPI()

cursos = []

@app.get("/bienvenida")
def obtener_mensaje():
    return "Bienvenido a nuestra plataforma"

@app.get("/cursos")
def obtener_curso():
    return cursos

@app.get("/docente")
def obtener_docente():
    return "El docente es A. Lara"

@app.get("/saludo/{nombre}")
def saludar(nombre):
    return "hola " + nombre

@app.get("/inicio/menu")
def otro_metodo():
    return "este es otro ejemplo"

@app.get("/inicio")
def otro_metodo():
    return "este es un inicio de algo"


@app.post("/curso")
def crear_curso(nombre, duracion):
    curso = {
        "nombre": nombre,
        "duracion": duracion
    }

    cursos.append(curso)
    return {
        "mensaje": "curso creado exitosamente",
        "curso": curso
    }