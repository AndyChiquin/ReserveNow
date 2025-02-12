require('dotenv').config();
const express = require('express');
const cors = require('cors');
const createBlockedRoutes = require('./routes/createBlockedRoutes');
const sequelize = require('./config/db');

const app = express();
app.use(cors());
app.use(express.json());
app.use('/api/blocked-users', createBlockedRoutes);

// Sincronizar la base de datos
sequelize.sync().then(() => {
  app.listen(process.env.PORT || 8010, () => {
    console.log(`🚀 Blocked Users Create Service running on port ${process.env.PORT || 8010}`);
  });
});
