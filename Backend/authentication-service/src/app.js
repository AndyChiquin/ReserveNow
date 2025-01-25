const express = require('express');
const bodyParser = require('body-parser');
const createUser = require('./business/create/createUser');
const getUsers = require('./business/read/getUsers');
const getUser = require('./business/read/getUser');
const updateUser = require('./business/update/updateUser');
const deleteUser = require('./business/delete/deleteUser');
const loginUser = require('./business/login/loginUser');


const app = express();
app.use(bodyParser.json());

const pool = require('./database/db');

// Probar conexión a la base de datos
pool.query('SELECT NOW()', (err, res) => {
  if (err) {
    console.error('Error al conectar a la base de datos:', err);
  } else {
    console.log('Conexión exitosa a la base de datos. Fecha y hora del servidor:', res.rows[0].now);
  }
});


app.post('/auth/login', loginUser);
 
app.post('/auth/users', createUser);       // Create user
app.get('/auth/users', getUsers);         // Get all users
app.get('/auth/users/:id', getUser);      // Get user by ID 
app.put('/auth/users/:id', updateUser);   // Update user 
app.delete('/auth/users/:id', deleteUser);// Delete user

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
