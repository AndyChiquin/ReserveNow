const pool = require('../../database/db');

const getReservationById = async (req, res) => {
  try {
    const { id } = req.params;

    console.log(`GET /reservations/${id} called`);

    const query = `SELECT * FROM reservations WHERE id = $1`;
    const result = await pool.query(query, [id]);

    if (result.rowCount === 0) {
      return res.status(404).json({ error: 'Reservation not found' });
    }

    res.status(200).json(result.rows[0]);
  } catch (error) {
    console.error('Error fetching reservation:', error.message);
    res.status(500).json({ error: 'Error fetching reservation', details: error.message });
  }
};

module.exports = getReservationById;
