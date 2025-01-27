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
    console.error('Error connecting to the database:', err);
  } else {
    console.log('Successful database connection. Server date and time:', res.rows[0].now);
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
  console.log(`Server running on http://localhost:${PORT}`);
});
