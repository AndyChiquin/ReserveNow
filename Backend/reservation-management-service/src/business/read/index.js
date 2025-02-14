const express = require("express");
const bodyParser = require("body-parser");
const getReservations = require("./getReservations");
const getReservationById = require("./getReservationById");
const pool = require("../../database/db"); // ✅ DRY: Single database connection instance.

const app = express();
app.use(bodyParser.json()); // ✅ DRY: Middleware is applied once for the entire app.

function checkDatabaseConnection() {
  /** ✅ DRY: Function to handle database connection check */
  pool.query("SELECT NOW()", (err, res) => {
    if (err) {
      console.error("Error connecting to the database:", err);
    } else {
      console.log("Successful database connection:", res.rows[0].now);
    }
  });
}

checkDatabaseConnection(); // ✅ DRY: Reusable function to verify database connection.

app.get("/reservations", getReservations);
app.get("/reservations/:id", getReservationById);

const PORT = process.env.PORT || 3101;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Read service running on port ${PORT}`); // ✅ DRY: Single log message for service start.
});
