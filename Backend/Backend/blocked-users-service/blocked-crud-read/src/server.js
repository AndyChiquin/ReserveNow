require('dotenv').config();
const express = require('express');
const cors = require('cors');
const readBlockedRoutes = require('./routes/readBlockedRoutes');
const sequelize = require('./config/db');

const app = express();
app.use(cors());
app.use(express.json());
app.use('/api/blocked-users', readBlockedRoutes);

// Sincronizar la base de datos
sequelize.sync().then(() => {
  app.listen(process.env.PORT || 8011, () => {
    console.log(`🚀 Blocked Users Read Service running on port ${process.env.PORT || 8011}`);
  });
});
