# Usa la imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia toda la aplicación dentro del contenedor
COPY . /app

# Expone el puerto que usará el servicio
EXPOSE 8000

# Ejecuta la aplicación
CMD ["uvicorn", "app.domain.create.main:app", "--host", "0.0.0.0", "--port", "8001"]
