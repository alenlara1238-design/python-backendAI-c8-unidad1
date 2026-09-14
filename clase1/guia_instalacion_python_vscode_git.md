# Configuración de Entorno para Python y VS Code

## 1. Instalación de Anaconda (Python)

### Sitio oficial de descarga
- https://www.anaconda.com/download

### Verificar instalación

Abrir una terminal y ejecutar:

```bash
conda --version
```

También puedes verificar Python:

```bash
python --version
```

o:

```bash
python3 --version
```

### Configuración inicial recomendada

Actualizar conda:

```bash
conda update conda
```

Crear un entorno virtual:

```bash
conda create -n mi_entorno python=3.12
```

Activar entorno:

```bash
conda activate mi_entorno
```

Desactivar entorno:

```bash
conda deactivate
```

---

# 2. Instalación de Visual Studio Code

## Sitio oficial de descarga
- https://code.visualstudio.com/

## Verificar instalación

Abrir una terminal y ejecutar:

```bash
code --version
```

> Si el comando `code` no funciona:
>
> - Abrir VS Code
> - Presionar `Ctrl + Shift + P`
> - Buscar:
>
> ```text
> Shell Command: Install 'code' command in PATH
> ```

---

# 3. Git y GitHub

## Instalación de Git

### Sitio oficial
- https://git-scm.com/downloads

## Verificar instalación

```bash
git --version
```

---

# Configuración inicial de Git

## Configurar nombre de usuario

```bash
git config --global user.name "Tu Nombre"
```

## Configurar correo electrónico

```bash
git config --global user.email "correo@ejemplo.com"
```

## Ver configuración actual

```bash
git config --list
```

---

# Comandos básicos de Git

## Inicializar repositorio

```bash
git init
```

## Ver estado del repositorio

```bash
git status
```

## Agregar archivos

Agregar un archivo:

```bash
git add archivo.py
```

Agregar todos los archivos:

```bash
git add .
```

## Crear commit

```bash
git commit -m "Mensaje del commit"
```

## Ver historial

```bash
git log
```

## Conectar repositorio remoto

```bash
git remote add origin URL_DEL_REPOSITORIO
```

## Subir cambios a GitHub

Primera vez:

```bash
git push -u origin main
```

Siguientes veces:

```bash
git push
```

## Descargar cambios

```bash
git pull
```

## Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

# GitHub

## Sitio oficial
- https://github.com/

## Recomendaciones iniciales

- Crear cuenta en GitHub
- Configurar autenticación
- Crear un repositorio
- Conectar Git local con GitHub

---

# 4. Extensiones recomendadas para VS Code

## Python Extension Pack
- https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack

## Python Snippets 3
- https://marketplace.visualstudio.com/items?itemName=frhtylcn.pythonsnippets

## Python Path
- https://marketplace.visualstudio.com/items?itemName=mgesbert.python-path

## Python Debugger
- https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy

## Python Notebook
- https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

---

# Verificar entorno completo

## Verificar Python

```bash
python --version
```

## Verificar pip

```bash
pip --version
```

## Verificar conda

```bash
conda --version
```

## Verificar Git

```bash
git --version
```

## Verificar VS Code

```bash
code --version
```

---

# Recomendaciones finales

- Reiniciar el computador después de las instalaciones principales.
- Mantener Python, Git y VS Code actualizados.
- Utilizar entornos virtuales para cada proyecto.
- Instalar extensiones oficiales desde el Marketplace de VS Code.
