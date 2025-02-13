# Usar Node.js como base
FROM node:18

# Crear el directorio de la aplicación
WORKDIR /app

# Copiar archivos al contenedor
COPY package.json package-lock.json ./

RUN npm install

# Copiar el resto de los archivos
COPY src /app/src

# Exponer el puerto del servicio
EXPOSE 3005

# Comando para ejecutar la aplicación
CMD ["node", "src/business/register/index.js"]
