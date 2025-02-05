const express = require('express');
const bodyParser = require('body-parser');
const getUsers = require('./getUsers');
const getUser = require('./getUser');
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

app.get('/auth/users', getUsers);     
app.get('/auth/users/:id', getUser);   

const PORT = process.env.PORT || 3001;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Read service running on port ${PORT}`);
});
