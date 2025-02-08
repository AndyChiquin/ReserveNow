# Usar una imagen base de Python optimizada
FROM python:3.9-slim

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos de dependencias e instalar las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del microservicio al contenedor
COPY . .

# Exponer el puerto 8001 (el mismo configurado en FastAPI)
EXPOSE 8001

# Comando para iniciar el servidor
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8001"]
