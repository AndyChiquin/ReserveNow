require("dotenv").config(); // Cargar las variables de entorno
const express = require('express');
const bodyParser = require('body-parser');
const loginUser = require('./loginUser');
const pool = require('../../database/db');
const cors = require("cors");


const app = express();
app.use(bodyParser.json());
app.use(cors());  
app.use(express.json()); 

pool.query('SELECT NOW()', (err, res) => {
  if (err) {
    console.error('Error connecting to the database:', err);
  } else {
    console.log('Successful database connection:', res.rows[0].now);
  }
});

app.post('/auth/login', loginUser);

const PORT = process.env.PORT || 3004;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Login service running on port ${PORT}`);
});
