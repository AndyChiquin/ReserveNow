const pool = require('../../database/db');

const getReservations = async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM reservations;');
    res.status(200).json(result.rows);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

module.exports = getReservations;
