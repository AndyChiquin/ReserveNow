FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY app /src/app

EXPOSE 3000

CMD ["node", "src/business/create/index.js"]
