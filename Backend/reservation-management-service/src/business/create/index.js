const express = require("express");
const bodyParser = require("body-parser");
const createReservation = require("./createReservation"); // ✅ SRP: Handles only reservation creation logic.
const pool = require("../../database/db"); // ✅ SRP: Handles only database connection.

const app = express();
app.use(bodyParser.json());

pool.query("SELECT NOW()", (err, res) => {
  if (err) {
    console.error("Error connecting to the database:", err);
  } else {
    console.log("Successful database connection:", res.rows[0].now);
  }
});

app.post("/reservations", createReservation); // ✅ SRP: Routes are responsible only for handling requests.

const PORT = process.env.PORT || 3100;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Create service running on port ${PORT}`); // ✅ SRP: Logging responsibility.
});
