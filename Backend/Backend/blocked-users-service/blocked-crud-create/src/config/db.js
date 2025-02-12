require('dotenv').config();
const { Sequelize } = require('sequelize');

console.log('🔍 Verificando variables de entorno...');
console.log('DB_PASSWORD:', `"${process.env.DB_PASSWORD}"`);  // Esto imprimirá la contraseña en la consola

if (!process.env.DB_PASSWORD || typeof process.env.DB_PASSWORD !== 'string') {
  console.error('❌ ERROR: DB_PASSWORD no está definida o no es un string.');
  process.exit(1);
}

const sequelize = new Sequelize(
  process.env.DB_NAME,
  process.env.DB_USER,
  process.env.DB_PASSWORD.trim(),  // Asegura que no haya espacios en blanco
  {
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    dialect: 'postgres',
    dialectOptions: {
      ssl: {
        require: true,
        rejectUnauthorized: false
      }
    },
    logging: false
  }
);

sequelize.authenticate()
  .then(() => console.log('✅ Connected to PostgreSQL - Blocked Users DB'))
  .catch(err => console.error('❌ Failed to connect to PostgreSQL:', err));

module.exports = sequelize;
