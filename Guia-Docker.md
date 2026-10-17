# 🐳 Guía de comandos Docker

**Descripción:** Manual de referencia de los principales comandos de Docker, con sintaxis, ejemplos y explicaciones prácticas.

**Objetivo:** Aprender a administrar imágenes, contenedores, redes, volúmenes y aplicaciones utilizando Docker CLI.

---

## 📚 Índice

1. [Introducción a Docker](#1-introducción-a-docker)
2. [Conceptos básicos](#2-conceptos-básicos)
3. [Comandos básicos](#3-comandos-básicos)
4. [Gestión de imágenes](#4-gestión-de-imágenes)
5. [Gestión de contenedores](#5-gestión-de-contenedores)
6. [Construcción de imágenes con Dockerfile](#6-construcción-de-imágenes-con-dockerfile)
7. [Puertos y acceso a localhost](#7-puertos-y-acceso-a-localhost)
8. [Volúmenes y persistencia de datos](#8-volúmenes-y-persistencia-de-datos)
9. [Redes de Docker](#9-redes-de-docker)
10. [Ejecución de comandos y depuración](#10-ejecución-de-comandos-y-depuración)
11. [Docker Compose](#11-docker-compose)
12. [Limpieza de recursos](#12-limpieza-de-recursos)
13. [Errores comunes](#13-errores-comunes)
14. [Tabla de consulta rápida](#14-tabla-de-consulta-rápida)
15. [Flujo de trabajo práctico](#15-flujo-de-trabajo-práctico)

---

## 1. Introducción a Docker

Docker es una plataforma que permite desarrollar, distribuir y ejecutar aplicaciones dentro de contenedores.

Los contenedores incluyen la aplicación y los elementos necesarios para ejecutarla, lo que ayuda a mantener un entorno consistente entre diferentes equipos.

### ¿Para qué sirve Docker?

- Ejecutar aplicaciones sin instalar todas sus dependencias directamente en el sistema anfitrión.
- Crear entornos de desarrollo reproducibles.
- Distribuir aplicaciones mediante imágenes.
- Ejecutar varios servicios de manera aislada.
- Facilitar el despliegue de aplicaciones.

### Requisitos previos

- Tener Docker Desktop instalado en Windows o macOS, o Docker Engine instalado en Linux.
- Comprobar que el motor de Docker está iniciado.
- Tener acceso a una terminal, como PowerShell, CMD o una terminal de Linux.

---

## 2. Conceptos básicos

| Concepto | Descripción |
|---|---|
| Imagen | Plantilla que contiene los elementos necesarios para crear un contenedor. |
| Contenedor | Instancia ejecutable de una imagen. |
| Dockerfile | Archivo con instrucciones para construir una imagen. |
| Volumen | Mecanismo para conservar datos fuera del ciclo de vida de un contenedor. |
| Red | Permite la comunicación entre contenedores y otros servicios. |
| Registro | Servicio que almacena y distribuye imágenes, como Docker Hub. |
| Docker Compose | Herramienta para definir y administrar aplicaciones con varios servicios. |
| Puerto | Punto de comunicación que puede publicarse entre el contenedor y el host. |

### Diferencia entre imagen y contenedor

Una imagen funciona como una plantilla. Un contenedor es una instancia creada a partir de esa plantilla.

Por ejemplo:

```bash
docker pull nginx
docker run -d --name mi_servidor nginx
```

El primer comando descarga la imagen de Nginx. El segundo crea y ejecuta un contenedor a partir de ella.

---

## 3. Comandos básicos

### 3.1. Consultar la versión

```bash
docker --version
```

Muestra la versión instalada de Docker CLI.

### 3.2. Consultar información del sistema

```bash
docker info
```

Muestra información del entorno Docker, incluyendo datos del motor, contenedores e imágenes.

### 3.3. Consultar la ayuda

```bash
docker --help
```

Muestra los comandos generales disponibles.

También puedes consultar la ayuda de un comando específico:

```bash
docker run --help
```

### 3.4. Comprobar el funcionamiento de Docker

```bash
docker run hello-world
```

Descarga la imagen `hello-world` si es necesario, crea un contenedor y ejecuta un programa que muestra un mensaje de prueba.

### 3.5. Consultar la versión del servidor

```bash
docker version
```

Muestra información de la versión del cliente y del servidor Docker. Si el motor no está disponible, la consulta del servidor puede fallar.

---

## 4. Gestión de imágenes

Las imágenes contienen las instrucciones, archivos y dependencias que necesita una aplicación para ejecutarse.

### 4.1. Descargar una imagen

```bash
docker pull python:3.12-slim
```

Descarga la imagen de Python con la etiqueta `3.12-slim`.

**Sintaxis general:**

```bash
docker pull nombre_imagen:etiqueta
```

### 4.2. Listar imágenes

```bash
docker images
```

Muestra las imágenes disponibles localmente.

Otra forma de consultar las imágenes es:

```bash
docker image ls
```

### 4.3. Buscar imágenes en Docker Hub

```bash
docker search nginx
```

Busca imágenes relacionadas con Nginx en Docker Hub.

### 4.4. Eliminar una imagen

```bash
docker rmi nombre_imagen:etiqueta
```

Elimina una imagen local cuando no existen dependencias que impidan su eliminación.

Ejemplo:

```bash
docker rmi python:3.12-slim
```

### 4.5. Consultar las capas de una imagen

```bash
docker history nombre_imagen:etiqueta
```

Muestra el historial de capas de una imagen.

### 4.6. Inspeccionar una imagen

```bash
docker image inspect nombre_imagen:etiqueta
```

Muestra información detallada de la imagen, como su configuración, arquitectura y metadatos.

---

## 5. Gestión de contenedores

Los contenedores permiten ejecutar aplicaciones de forma aislada a partir de imágenes.

### 5.1. Crear y ejecutar un contenedor

```bash
docker run hello-world
```

Crea y ejecuta un contenedor con la imagen `hello-world`.

### 5.2. Ejecutar un contenedor en segundo plano

```bash
docker run -d --name mi_contenedor nginx
```

**Explicación de los parámetros:**

| Parámetro | Función |
|---|---|
| `run` | Crea y ejecuta un contenedor. |
| `-d` | Ejecuta el contenedor en segundo plano. |
| `--name` | Asigna un nombre al contenedor. |
| `nginx` | Especifica la imagen que se utilizará. |

### 5.3. Listar contenedores activos

```bash
docker ps
```

Muestra únicamente los contenedores en ejecución.

### 5.4. Listar todos los contenedores

```bash
docker ps -a
```

Muestra los contenedores activos y detenidos.

### 5.5. Detener un contenedor

```bash
docker stop mi_contenedor
```

Detiene el contenedor de forma controlada.

### 5.6. Iniciar un contenedor detenido

```bash
docker start mi_contenedor
```

Inicia nuevamente un contenedor existente.

### 5.7. Reiniciar un contenedor

```bash
docker restart mi_contenedor
```

Detiene y vuelve a iniciar el contenedor.

### 5.8. Eliminar un contenedor

```bash
docker rm mi_contenedor
```

Elimina un contenedor detenido.

Para detener y eliminar un contenedor en ejecución:

```bash
docker rm -f mi_contenedor
```

**Precaución:** `-f` fuerza la eliminación y detiene el contenedor si es necesario.

### 5.9. Asignar un nombre a un contenedor

```bash
docker run -d --name servidor_web nginx
```

El parámetro `--name` permite utilizar un nombre fácil de recordar en otros comandos.

### 5.10. Consultar el estado de los contenedores

```bash
docker ps -a
```

Revisa la columna `STATUS` para identificar si un contenedor está ejecutándose, se detuvo o terminó.

---

## 6. Construcción de imágenes con Dockerfile

Un Dockerfile contiene las instrucciones utilizadas para construir una imagen personalizada.

### 6.1. Crear un Dockerfile

Ejemplo de un Dockerfile para una aplicación Python:

```dockerfile
# Selecciona una imagen base de Python.
FROM python:3.12-slim

# Define el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copia el archivo de dependencias.
COPY requirements.txt .

# Instala las dependencias de Python.
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación.
COPY . .

# Indica el puerto que utiliza la aplicación.
EXPOSE 5000

# Define el comando de inicio.
CMD ["python", "app.py"]
```

**Descripción de las instrucciones:**

| Instrucción | Función |
|---|---|
| `FROM` | Selecciona la imagen base. |
| `WORKDIR` | Define el directorio de trabajo. |
| `COPY` | Copia archivos al sistema de archivos de la imagen. |
| `RUN` | Ejecuta comandos durante la construcción de la imagen. |
| `EXPOSE` | Documenta el puerto previsto para la aplicación. No publica el puerto por sí solo. |
| `CMD` | Define el comando predeterminado al ejecutar el contenedor. |

### 6.2. Construir una imagen

Desde el directorio donde se encuentra el Dockerfile:

```bash
docker build -t mi_aplicacion:1.0 .
```

**Explicación:**

- `build`: construye una imagen.
- `-t`: asigna un nombre y una etiqueta.
- `mi_aplicacion:1.0`: nombre y versión de la imagen.
- `.`: utiliza el directorio actual como contexto de construcción.

### 6.3. Construir una imagen desde otro Dockerfile

```bash
docker build -f Dockerfile.dev -t mi_aplicacion:dev .
```

Utiliza `Dockerfile.dev` en lugar del Dockerfile predeterminado.

### 6.4. Reconstruir una imagen sin utilizar la caché

```bash
docker build --no-cache -t mi_aplicacion:1.0 .
```

Evita utilizar la caché de las instrucciones de construcción. Es útil cuando necesitas reconstruir las capas sin reutilizar los resultados almacenados en caché.

---

## 7. Puertos y acceso a localhost

Para acceder desde el navegador a una aplicación que se ejecuta en un contenedor, normalmente necesitas publicar el puerto correspondiente.

### 7.1. Publicar un puerto

```bash
docker run -d -p 8080:80 --name mi_web nginx
```

Publica el puerto 80 del contenedor en el puerto 8080 del host.

Puedes acceder desde el navegador:

```text
http://localhost:8080
```

**Sintaxis del parámetro `-p`:**

```text
-p puerto_host:puerto_contenedor
```

Por ejemplo:

```bash
docker run -d -p 5000:5000 --name mi_api mi_aplicacion:1.0
```

Publica el puerto 5000 del contenedor en el puerto 5000 del host.

**Importante:** para acceder a una aplicación Flask desde fuera del contenedor, el servidor normalmente debe escuchar en `0.0.0.0` dentro del contenedor, no únicamente en `127.0.0.1`.

### 7.2. Consultar los puertos publicados

```bash
docker port mi_web
```

Muestra los mapeos de puertos del contenedor.

### 7.3. Ejecutar un contenedor sin publicar puertos

```bash
docker run -d --name mi_web_interna nginx
```

El contenedor se ejecuta sin publicar puertos en el host. Esto no impide necesariamente que otros contenedores puedan comunicarse con él mediante una red adecuada.

---

## 8. Volúmenes y persistencia de datos

Los volúmenes permiten conservar datos incluso cuando se elimina un contenedor.

### 8.1. Crear un volumen

```bash
docker volume create mis_datos
```

Crea un volumen administrado por Docker.

### 8.2. Listar volúmenes

```bash
docker volume ls
```

Muestra los volúmenes disponibles.

### 8.3. Inspeccionar un volumen

```bash
docker volume inspect mis_datos
```

Muestra información del volumen.

### 8.4. Montar un volumen en un contenedor

```bash
docker run -d --name mi_nginx -v mis_datos:/datos nginx
```

Monta el volumen `mis_datos` en la ruta `/datos` dentro del contenedor.

**Sintaxis:**

```text
-v nombre_volumen:ruta_contenedor
```

### 8.5. Eliminar un volumen

```bash
docker volume rm mis_datos
```

Elimina el volumen si no está en uso.

**Precaución:** eliminar un volumen puede borrar los datos almacenados en él.

### 8.6. Montar una carpeta del equipo

```bash
docker run --rm -it -v "${PWD}:/app" -w /app python:3.12-slim python --version
```

Monta el directorio actual en `/app` y ejecuta una consulta de versión de Python.

En PowerShell, `${PWD}` hace referencia al directorio actual. En otras terminales puede variar la sintaxis de la ruta.

---

## 9. Redes de Docker

Las redes permiten que los contenedores se comuniquen entre sí.

### 9.1. Listar redes

```bash
docker network ls
```

Muestra las redes existentes.

### 9.2. Crear una red

```bash
docker network create mi_red
```

Crea una red administrada por Docker.

### 9.3. Ejecutar un contenedor en una red

```bash
docker run -d --name servidor --network mi_red nginx
```

Conecta el contenedor a la red `mi_red`.

### 9.4. Conectar un contenedor a una red existente

```bash
docker network connect mi_red mi_contenedor
```

Conecta un contenedor existente a la red especificada.

### 9.5. Inspeccionar una red

```bash
docker network inspect mi_red
```

Muestra información detallada de la red y los contenedores conectados.

### 9.6. Eliminar una red

```bash
docker network rm mi_red
```

Elimina una red que ya no esté en uso.

---

## 10. Ejecución de comandos y depuración

Estos comandos son útiles para comprobar qué sucede dentro de un contenedor.

### 10.1. Consultar los registros

```bash
docker logs mi_contenedor
```

Muestra los registros del contenedor.

Para seguirlos en tiempo real:

```bash
docker logs -f mi_contenedor
```

Para mostrar las últimas 100 líneas:

```bash
docker logs --tail 100 mi_contenedor
```

### 10.2. Ejecutar un comando dentro de un contenedor

```bash
docker exec -it mi_contenedor sh
```

Abre una sesión interactiva de `sh`, si está disponible dentro del contenedor.

En imágenes que incluyen Bash puedes utilizar:

```bash
docker exec -it mi_contenedor bash
```

### 10.3. Ejecutar un comando sin abrir una terminal

```bash
docker exec mi_contenedor ls
```

Ejecuta `ls` dentro del contenedor, siempre que el ejecutable esté disponible.

### 10.4. Inspeccionar un contenedor

```bash
docker inspect mi_contenedor
```

Muestra información detallada del contenedor, como su configuración, estado, red y montajes.

### 10.5. Consultar el consumo de recursos

```bash
docker stats
```

Muestra estadísticas de uso de CPU, memoria, red y otros recursos de los contenedores en ejecución.

### 10.6. Consultar los procesos de un contenedor

```bash
docker top mi_contenedor
```

Muestra los procesos que se ejecutan dentro del contenedor.

---

## 11. Docker Compose

Docker Compose permite definir y administrar aplicaciones con varios servicios mediante un archivo YAML.

### 11.1. Ejemplo de `compose.yaml`

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
```

Este archivo define un servicio llamado `web` que utiliza Nginx y publica el puerto 80 del contenedor en el puerto 8080 del host.

### 11.2. Iniciar los servicios

```bash
docker compose up -d
```

Crea e inicia los servicios definidos en el archivo Compose.

### 11.3. Consultar los servicios

```bash
docker compose ps
```

Muestra el estado de los servicios administrados por Compose.

### 11.4. Consultar los registros

```bash
docker compose logs
```

Muestra los registros de los servicios.

Para seguirlos en tiempo real:

```bash
docker compose logs -f
```

### 11.5. Detener los servicios

```bash
docker compose stop
```

Detiene los servicios sin eliminarlos.

### 11.6. Detener y eliminar los recursos del proyecto

```bash
docker compose down
```

Detiene y elimina los contenedores y las redes creadas por Compose para el proyecto. Los volúmenes nombrados no se eliminan de forma predeterminada.

---

## 12. Limpieza de recursos

Docker permite eliminar recursos que ya no se necesitan. Antes de ejecutar estos comandos, comprueba qué elementos serán afectados.

### 12.1. Eliminar contenedores detenidos

```bash
docker container prune
```

Elimina los contenedores detenidos que cumplen los criterios de limpieza.

### 12.2. Eliminar imágenes no utilizadas

```bash
docker image prune
```

Elimina las imágenes no utilizadas que cumplen los criterios predeterminados de limpieza.

### 12.3. Eliminar redes no utilizadas

```bash
docker network prune
```

Elimina las redes que no están conectadas a contenedores.

### 12.4. Eliminar volúmenes no utilizados

```bash
docker volume prune
```

Elimina los volúmenes que Docker considera no utilizados. Revisa cuidadosamente su contenido antes de hacerlo.

### 12.5. Limpiar varios recursos

```bash
docker system prune
```

Elimina recursos no utilizados según las reglas de limpieza de Docker, como contenedores detenidos, redes no utilizadas, imágenes sin referencias y caché de construcción.

Para incluir imágenes no utilizadas por ningún contenedor:

```bash
docker system prune -a
```

**Precaución:** los comandos de limpieza pueden eliminar recursos que quieras conservar. No utilices opciones adicionales sin comprender su efecto.

---

## 13. Errores comunes

### 13.1. Docker no está iniciado

**Síntoma:** el cliente no puede conectarse al servidor Docker.

**Solución:**

1. Comprueba que Docker Desktop o Docker Engine esté iniciado.
2. Ejecuta `docker version`.
3. Revisa el mensaje de error si la conexión sigue fallando.

### 13.2. El puerto ya está en uso

**Síntoma:** Docker no puede publicar el puerto solicitado porque otro proceso ya lo utiliza.

**Solución:** selecciona otro puerto del host.

```bash
docker run -d -p 8081:80 --name mi_web nginx
```

Accede a `http://localhost:8081`.

### 13.3. El contenedor se detiene inmediatamente

**Síntoma:** el contenedor aparece en `docker ps -a`, pero no en `docker ps`.

**Solución:**

```bash
docker logs mi_contenedor
```

Revisa los registros para identificar si la aplicación terminó, encontró un error o recibió una señal de salida.

### 13.4. No se encuentra el Dockerfile

**Síntoma:** Docker no puede localizar el archivo necesario para construir la imagen.

**Solución:** sitúate en el directorio correcto y comprueba que el archivo se llame `Dockerfile`, o especifica otro nombre con `-f`.

```bash
docker build -t mi_aplicacion .
```

### 13.5. No se encuentra una imagen

**Síntoma:** Docker no puede utilizar la imagen indicada.

**Solución:** comprueba el nombre y la etiqueta.

```bash
docker pull nginx:alpine
```

### 13.6. No puedes acceder a una aplicación desde localhost

Comprueba:

1. Que el contenedor esté en ejecución.
2. Que el puerto se haya publicado correctamente.
3. Que la aplicación escuche en la interfaz adecuada dentro del contenedor.
4. Que los registros no indiquen errores.

Consulta el mapeo de puertos con:

```bash
docker port mi_contenedor
```

---

## 14. Tabla de consulta rápida

| Comando | Función |
|---|---|
| `docker --version` | Consultar la versión de Docker CLI. |
| `docker version` | Consultar versiones del cliente y servidor. |
| `docker info` | Consultar información del motor. |
| `docker pull` | Descargar una imagen. |
| `docker images` | Listar imágenes locales. |
| `docker build` | Construir una imagen. |
| `docker run` | Crear y ejecutar un contenedor. |
| `docker ps` | Listar contenedores en ejecución. |
| `docker ps -a` | Listar todos los contenedores. |
| `docker stop` | Detener un contenedor. |
| `docker start` | Iniciar un contenedor detenido. |
| `docker restart` | Reiniciar un contenedor. |
| `docker rm` | Eliminar un contenedor. |
| `docker rmi` | Eliminar una imagen. |
| `docker logs` | Consultar registros. |
| `docker exec` | Ejecutar un comando dentro del contenedor. |
| `docker inspect` | Consultar información detallada. |
| `docker stats` | Consultar el consumo de recursos. |
| `docker volume ls` | Listar volúmenes. |
| `docker network ls` | Listar redes. |
| `docker compose up -d` | Iniciar servicios de Compose. |
| `docker compose down` | Detener y eliminar recursos del proyecto Compose. |
| `docker system prune` | Limpiar recursos no utilizados. |

---

## 15. Flujo de trabajo práctico

El siguiente ejemplo muestra el proceso básico para construir una imagen y ejecutar una aplicación.

### Paso 1. Crear el proyecto

```text
mi_proyecto/
├── Dockerfile
└── app.py
```

### Paso 2. Crear `app.py`

```python
print("Hola Mundo desde Docker")
```

### Paso 3. Crear el Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

### Paso 4. Construir la imagen

Ejecuta el comando desde el directorio `mi_proyecto`:

```bash
docker build -t hola-python:1.0 .
```

### Paso 5. Ejecutar el contenedor

```bash
docker run --name hola-python hola-python:1.0
```

El programa imprimirá:

```text
Hola Mundo desde Docker
```

Como el programa termina después de imprimir el mensaje, el contenedor también finalizará.

### Paso 6. Consultar el contenedor

```bash
docker ps -a
```

El contenedor aparecerá con un estado de finalización.

### Paso 7. Eliminar el contenedor

```bash
docker rm hola-python
```

La imagen `hola-python:1.0` seguirá disponible para ejecutar nuevos contenedores.

---

## 📌 Recomendaciones finales

- Utiliza nombres descriptivos para las imágenes y los contenedores.
- Organiza cada proyecto en su propio directorio.
- Incluye un archivo `.dockerignore` para excluir archivos innecesarios del contexto de construcción.
- Consulta los registros antes de intentar corregir un contenedor que falla.
- Usa volúmenes cuando necesites conservar datos.
- Evita eliminar volúmenes o imágenes sin comprobar sus dependencias.
- Consulta la [documentación oficial de Docker](https://docs.docker.com/) para conocer las opciones completas y actualizadas.

---

**Fin de la guía de comandos Docker.**
