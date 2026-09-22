from fastapi import FastAPI
from sqlalchemy import text

from database import engine

app = FastAPI()

cursos = []


# creemos una ruta de tipo prueba
@app.get("/test-db")
def test_database():
    with engine.connect() as connection:
      result = connection.execute(text("SELECT 1"))
    return {
        "database": result.scalar()
    }






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

# PUT: actualiza todos los datos de un recurso.
@app.put("/curso/{nombre}")  
def actualizar_curso(nombre: str, nuevo_nombre: str, nueva_duracion: str):
    # 1. Buscamos el curso (por nombre)
    for curso in cursos:
        # SI existe, entonces...
       if curso["nombre"] == nombre:
            # Cambia su antiguo nombre, por el nuevo:
            curso["nombre"] = nuevo_nombre
            # Cambia su antigua duracion, por la nueva:
            curso["duracion"] = nueva_duracion
            return {
                "mensaje": "curso actualizado exitosamente",
                "curso": curso
            }
    
    return {
        "mensaje": "curso no encontrado"
    }

@app.patch("/curso/{nombre}")
def modificar_curso(nombre: str, nueva_duracion: str):
    for curso in cursos:
        if curso["nombre"] == nombre:
            curso["duracion"] = nueva_duracion
            return {
                "mensaje": "curso modificado exitosamente",
                "curso": curso
            }
    
    return {
        "mensaje": "curso no encontrado"
    }

@app.delete("/curso/{nombre}")
def eliminar_curso(nombre: str):
    for curso in cursos:
        if curso["nombre"] == nombre:
            cursos.remove(curso)
            return {
                "mensaje": "curso eliminado exitosamente"
            }
    return {
        "mensaje": "curso no encontrado"
    }