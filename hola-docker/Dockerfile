# 1. Descarga Linux con Python instalado
FROM python:3.12-slim

# 2. Crea la carpeta de trabajo
WORKDIR /app

# 3. Copia el archivo de requisitos dentro del contenedor
COPY requirements.txt .

# 4. PASO CLAVE: Ejecuta la instalación automática de dependencias adentro
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia tu archivo de código app.py adentro
COPY app.py .

# 6. Avisa que usaremos el puerto 5000
EXPOSE 5000

# 7. Comando para arrancar tu programa de Python
CMD ["python", "app.py"]
