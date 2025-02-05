const express = require('express');
const bodyParser = require('body-parser');
const createUser = require('./createUser');
const pool = require('../../database/db');

const app = express();
app.use(bodyParser.json());

pool.query('SELECT NOW()', (err, res) => {
  if (err) {
    console.error('Error connecting to the database:', err);
  } else {
    console.log('Successful database connection:', res.rows[0].now);
  }
});

app.post('/auth/users', createUser);

const PORT = process.env.PORT || 3000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Create service running on port ${PORT}`);
});
