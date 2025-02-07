const express = require("express");
const bodyParser = require("body-parser");
const modifyReservation = require("./modifyReservation");
const pool = require("../../database/db");

const app = express();
app.use(bodyParser.json());

// Verificar conexión con la base de datos
pool.query("SELECT NOW()", (err, res) => {
  if (err) {
    console.error("Error connecting to the database:", err);
  } else {
    console.log("Successful database connection:", res.rows[0].now);
  }
});

// Ruta para modificar una reservación
app.put("/reservations/:id", modifyReservation);

// Usar el puerto 3100 para que coincida con Docker
const PORT = process.env.PORT || 3102;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Update service running on port ${PORT}`);
});
