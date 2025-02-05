FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY src /app/src

EXPOSE 3101

CMD ["node", "src/business/create/index.js"]
