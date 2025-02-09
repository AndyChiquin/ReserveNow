# Usa la imagen oficial de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios para el microservicio
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente del microservicio
COPY . .

# Exponer el puerto correspondiente al servicio (5200)
EXPOSE 5200

# Comando para ejecutar el servicio
CMD ["python", "app/domain/create/createFeedback.py"]
