FROM python:3.9

# Instala las dependencias del sistema para ODBC y MSSQL
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    odbcinst \
    libodbc1 \
    libodbc2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5201

CMD ["python", "app/domain/read/readFeedback.py"]
