FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY src /app/src

EXPOSE 3104

CMD ["node", "src/business/update/index.js"]
