const express = require("express");
const bodyParser = require("body-parser");
const cancelReservation = require("./cancelReservation"); // ✅ KISS: Importing only the necessary module.
const pool = require("../../database/db"); // ✅ KISS: Direct and clear database connection.

const app = express();
app.use(bodyParser.json()); // ✅ KISS: Simple middleware for parsing JSON requests.

pool.query("SELECT NOW()", (err, res) => {
  if (err) {
    console.error("Error connecting to the database:", err);
  } else {
    console.log("Successful database connection:", res.rows[0].now);
  }
});

app.delete("/reservations/:id", cancelReservation); // ✅ KISS: Clear and concise route definition.

const PORT = process.env.PORT || 3103;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Delete service running on port ${PORT}`); // ✅ KISS: Simple logging message.
});
