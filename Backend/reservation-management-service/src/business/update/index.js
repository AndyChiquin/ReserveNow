const express = require("express");
const bodyParser = require("body-parser");
const modifyReservation = require("./modifyReservation"); // ✅ OCP: The route logic is delegated to a separate module.
const pool = require("../../database/db"); // ✅ OCP: Database connection is abstracted.

const app = express();
app.use(bodyParser.json()); // ✅ OCP: Middleware is applied once for all routes.

function checkDatabaseConnection() {
  /** ✅ OCP: Function responsible only for checking the database connection. */
  pool.query("SELECT NOW()", (err, res) => {
    if (err) {
      console.error("Error connecting to the database:", err);
    } else {
      console.log("Successful database connection:", res.rows[0].now);
    }
  });
}

checkDatabaseConnection(); // ✅ OCP: Reusable database connection check function.

app.put("/reservations/:id", modifyReservation); // ✅ OCP: Route is extendable without modifying app logic.

const PORT = process.env.PORT || 3102;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Update service running on port ${PORT}`); // ✅ OCP: Logging responsibility is separate.
});
