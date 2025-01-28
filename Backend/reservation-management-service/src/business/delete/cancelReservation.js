const pool = require('../../database/db');
const axios = require('axios');

const cancelReservation = async (req, res) => {
  try {
    const { id } = req.params;

    console.log(`DELETE /reservations/${id} called`);

    const reservationQuery = `SELECT * FROM reservations WHERE id = $1`;
    const reservationResult = await pool.query(reservationQuery, [id]);
    if (reservationResult.rowCount === 0) {
      return res.status(404).json({ error: 'Reservation not found' });
    }

    const reservation = reservationResult.rows[0];

    const cancelQuery = `
      UPDATE reservations
      SET status = 'CANCELLED'
      WHERE id = $1 RETURNING *;
    `;
    const cancelResult = await pool.query(cancelQuery, [id]);

    try {
      await axios.put(
        `http://127.0.0.1:8000/tables/${reservation.table_id}`,
        { status: 'available' },
        { headers: { 'Content-Type': 'application/json' } }
      );
      console.log(`Table ${reservation.table_id} updated to available.`);
    } catch (error) {
      console.error('Error updating table status:', error.message);
      return res.status(500).json({
        message: 'Reservation cancelled, but failed to update table status',
        reservation: cancelResult.rows[0],
        error: 'Error updating table status in tables-management',
      });
    }

    res.status(200).json({ message: 'Reservation cancelled', reservation: cancelResult.rows[0] });
  } catch (error) {
    console.error('Error cancelling reservation:', error.message);
    res.status(500).json({ error: 'Error cancelling reservation', details: error.message });
  }
};

module.exports = cancelReservation;
