# Usa la imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia y instala las dependencias
COPY ../../../../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente del servicio de lectura de mesas
COPY ../../../../app /app

# Expone el puerto en el que se ejecutará el servicio
EXPOSE 8002

# Comando para ejecutar el servicio de lectura
CMD ["uvicorn", "app.domain.read.main:app", "--host", "0.0.0.0", "--port", "8002"]
