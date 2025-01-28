const express = require('express');
const bodyParser = require('body-parser');
const createReservation = require('./business/create/createReservation');
const getReservations = require('./business/read/getReservations');
const modifyReservation = require('./business/update/modifyReservation');
const cancelReservation = require('./business/delete/cancelReservation');
const getReservationById = require('./business/read/getReservationById');


const app = express();
const PORT = process.env.PORT || 3001;

app.use(bodyParser.json()); 

app.post('/reservations', createReservation); 
app.get('/reservations', getReservations); 
app.get('/reservations/:id', getReservationById);
app.put('/reservations/:id', modifyReservation); 
app.delete('/reservations/:id', cancelReservation); 

app.get('/', (req, res) => {
  res.status(200).send('Reservation service is running');
});

app.listen(PORT, () => {
  console.log(`Reservation service running on http://localhost:${PORT}`);
});
