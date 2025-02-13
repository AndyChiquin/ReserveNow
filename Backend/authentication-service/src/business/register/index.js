const express = require("express");
const bodyParser = require("body-parser");
const registerUser = require("./registerUser");
const pool = require("../../database/db");
const cors = require("cors");

const app = express();
app.use(bodyParser.json());
app.use(cors());
app.use(express.json());

// Probar conexión a la base de datos
pool.query("SELECT NOW()", (err, res) => {
  if (err) {
    console.error("Error connecting to the database:", err);
  } else {
    console.log("Successful database connection:", res.rows[0].now);
  }
});

// Endpoint de registro
app.post("/auth/register", registerUser);

const PORT = process.env.PORT || 3005;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Register service running on port ${PORT}`);
});
