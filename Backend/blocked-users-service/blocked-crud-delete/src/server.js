require('dotenv').config();
const express = require('express');
const cors = require('cors');
const deleteBlockedRoutes = require('./routes/deleteBlockedRoutes');
const sequelize = require('./config/db');

const app = express();
app.use(cors());
app.use(express.json());
app.use('/api/blocked-users', deleteBlockedRoutes);

// Sincronizar la base de datos
sequelize.sync().then(() => {
  app.listen(process.env.PORT || 8013, () => {
    console.log(`🚀 Blocked Users Delete Service running on port ${process.env.PORT || 8013}`);
  });
});
