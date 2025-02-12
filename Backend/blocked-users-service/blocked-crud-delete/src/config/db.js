require('dotenv').config();
const { Sequelize } = require('sequelize');

const sequelize = new Sequelize(
  process.env.DB_NAME,
  process.env.DB_USER,
  process.env.DB_PASSWORD,
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

sequelize.sync({ alter: true })  // Mantiene la tabla actualizada
  .then(() => console.log('✅ Database synchronized for delete service'))
  .catch(err => console.error('❌ Sync Error:', err));

module.exports = sequelize;
