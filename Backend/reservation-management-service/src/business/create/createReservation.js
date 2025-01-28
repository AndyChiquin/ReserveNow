const pool = require('../../database/db');
const axios = require('axios');
const { isValid, parseISO } = require('date-fns');


const createReservation = async (req, res) => {
  try {
    const { userId, tableId, reservationDate } = req.body;

    if (!userId || !tableId || !reservationDate) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Validar el formato de la fecha
    const parsedDate = parseISO(reservationDate);
    if (!isValid(parsedDate)) {
      return res.status(400).json({ error: 'Invalid date format' });
    }
/*
    try {
      const authResponse = await axios.get(`http://localhost:3000/auth/users/${userId}`);
      if (authResponse.status !== 200) {
        return res.status(404).json({ error: 'User not found' });
      }
    } catch (error) {
      if (error.response && error.response.status === 404) {
        return res.status(404).json({ error: 'User not found' });
      }
      return res.status(500).json({ error: 'Error communicating with auth service', details: error.message });
    }
*/
    try {
      const tableResponse = await axios.get(`http://127.0.0.1:8000/tables/${tableId}`);
      const tableData = tableResponse.data;

      if (tableData.status !== 'available') {
        return res.status(409).json({ error: 'Table is not available' });
      }
    } catch (error) {
      console.error('Error communicating with tables service:', error.message);
      if (error.response?.status === 404) {
        return res.status(404).json({ error: 'Table not found' });
      }
      return res.status(500).json({ error: 'Error communicating with tables service' });
    }

    const checkQuery = `
      SELECT * FROM reservations
      WHERE table_id = $1 AND reservation_date = $2 AND status = 'ACTIVE';
    `;
    const checkResult = await pool.query(checkQuery, [tableId, reservationDate]);

    if (checkResult.rowCount > 0) {
      return res.status(409).json({ error: 'Table is already reserved at this time' });
    }

    const insertQuery = `
      INSERT INTO reservations (user_id, table_id, reservation_date, status)
      VALUES ($1, $2, $3, 'ACTIVE') RETURNING *;
    `;
    const insertResult = await pool.query(insertQuery, [userId, tableId, reservationDate]);

     // Actualizar el estado de la mesa a "reserved" en `tables-management`
     try {
      await axios.put(
        `http://127.0.0.1:8000/tables/${tableId}`,
        { status: 'reserved' },
        { headers: { 'Content-Type': 'application/json' } }
      );
    } catch (error) {
      console.error('Error updating table status:', error.message);
      // Si falla la actualización, la reservación sigue creada, pero se notifica el error
      return res.status(201).json({
        message: 'Reservation created, but failed to update table status',
        reservation: insertResult.rows[0],
        error: 'Error updating table status in tables-management',
      });
    }

    res.status(201).json({ message: 'Reservation created', reservation: insertResult.rows[0] });
  } catch (error) {
    console.error('Error creating reservation:', error.message);
    res.status(500).json({ error: 'Error creating reservation', details: error.message });
  }
};

module.exports = createReservation;
