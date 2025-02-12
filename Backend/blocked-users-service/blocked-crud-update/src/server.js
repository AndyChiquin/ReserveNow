require('dotenv').config();
const express = require('express');
const cors = require('cors');
const updateBlockedRoutes = require('./routes/updateBlockedRoutes');
const sequelize = require('./config/db');

const app = express();
app.use(cors());
app.use(express.json());
app.use('/api/blocked-users', updateBlockedRoutes);

sequelize.sync().then(() => {
  app.listen(8012, () => {
    console.log('🚀 Blocked Users Update Service running on port 8012');
  });
});
