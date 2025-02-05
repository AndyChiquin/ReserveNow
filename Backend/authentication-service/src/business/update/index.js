const express = require('express');
const bodyParser = require('body-parser');
const updateUser = require('./updateUser');
const pool = require('../database/db');

const app = express();
app.use(bodyParser.json());

pool.query('SELECT NOW()', (err, res) => {
  if (err) {
    console.error('Error connecting to the database:', err);
  } else {
    console.log('Successful database connection:', res.rows[0].now);
  }
});

app.put('/auth/users/:id', updateUser);

const PORT = process.env.PORT || 3002;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Update service running on port ${PORT}`);
});
