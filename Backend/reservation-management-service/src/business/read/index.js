const express = require("express");
const bodyParser = require("body-parser");
const getReservations = require("./getReservations");
const getReservationById = require("./getReservationById");
const pool = require("../../database/db");

const app = express();
app.use(bodyParser.json());

pool.query("SELECT NOW()", (err, res) => {
  if (err) {
    console.error("Error connecting to the database:", err);
  } else {
    console.log("Successful database connection:", res.rows[0].now);
  }
});

app.get("/reservations", getReservations);
app.get("/reservations/:id", getReservationById);

const PORT = process.env.PORT || 3101;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Read service running on port ${PORT}`);
});
