const express = require("express");
const createReservation = require("./createReservation");

const app = express();
app.use(express.json());

app.post("/reservations", createReservation);

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Create Reservation service running on port ${PORT}`);
});
