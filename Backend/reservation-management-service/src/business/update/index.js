const express = require("express");
const bodyParser = require("body-parser");
const modifyReservation = require("./modifyReservation");
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

app.put("/reservations/:id", modifyReservation);

const PORT = process.env.PORT || 3102;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Update service running on port ${PORT}`);
});
