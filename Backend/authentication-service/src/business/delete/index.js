const express = require('express');
const bodyParser = require('body-parser');
const deleteUser = require('./deleteUser');
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

app.delete('/auth/users/:id', deleteUser);

const PORT = process.env.PORT || 3003;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Delete service running on port ${PORT}`);
});
