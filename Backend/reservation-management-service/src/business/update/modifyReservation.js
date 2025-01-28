const pool = require('../../database/db');
const axios = require('axios');

const modifyReservation = async (req, res) => {
  try {
    const { id } = req.params;
    const { userId, tableId, reservationDate, status } = req.body;

    console.log(`PUT /reservations/${id} called with:`, req.body);

    const reservationQuery = `SELECT * FROM reservations WHERE id = $1`;
    const reservationResult = await pool.query(reservationQuery, [id]);
    if (reservationResult.rowCount === 0) {
      return res.status(404).json({ error: 'Reservation not found' });
    }
    const existingReservation = reservationResult.rows[0];

/*
    if (userId) {
      try {
        const authResponse = await axios.get(`http://localhost:3000/auth/users/${userId}`);
        if (authResponse.status !== 200) {
          return res.status(404).json({ error: 'User not found' });
        }
      } catch (error) {
        if (error.response && error.response.status === 404) {
          return res.status(404).json({ error: 'User not found' });
        }
        console.error('Error communicating with auth service:', error.message);
        return res.status(500).json({ error: 'Error communicating with auth service', details: error.message });
      }
    }
*/
    if (tableId) {
      try {
        const tableResponse = await axios.get(`http://127.0.0.1:8000/tables/${tableId}`);
        if (tableResponse.status !== 200) {
          return res.status(404).json({ error: 'Table not found' });
        }
      } catch (error) {
        if (error.response && error.response.status === 404) {
          return res.status(404).json({ error: 'Table not found' });
        }
        console.error('Error communicating with tables service:', error.message);
        return res.status(500).json({ error: 'Error communicating with tables service', details: error.message });
      }
    }

    if (tableId && reservationDate) {
      const checkQuery = `
        SELECT * FROM reservations
        WHERE table_id = $1 AND reservation_date = $2 AND status = 'ACTIVE' AND id != $3;
      `;
      const checkResult = await pool.query(checkQuery, [tableId, reservationDate, id]);
      if (checkResult.rowCount > 0) {
        return res.status(409).json({ error: 'Table is already reserved at this time' });
      }
    }

    const updateQuery = `
      UPDATE reservations
      SET 
        user_id = COALESCE($1, user_id),
        table_id = COALESCE($2, table_id),
        reservation_date = COALESCE($3, reservation_date),
        status = COALESCE($4, status)
      WHERE id = $5
      RETURNING *;
    `;
    const updateResult = await pool.query(updateQuery, [
      userId || null,
      tableId || null,
      reservationDate || null,
      status || null,
      id,
    ]);

    const updatedReservation = updateResult.rows[0];

     // Actualizar el estado de las mesas
     try {
      if (status === 'CANCELLED') {
        const activeReservationsQuery = `
          SELECT reservation_date FROM reservations
          WHERE table_id = $1 AND status = 'ACTIVE';
        `;
        const activeReservationsResult = await pool.query(activeReservationsQuery, [existingReservation.table_id]);

        // Revisar si todas las reservaciones activas son para una fecha distinta a la reservación cancelada
        const otherDates = activeReservationsResult.rows.some(
          (reservation) => reservation.reservation_date !== existingReservation.reservation_date
        );

        // Si no hay otras reservaciones activas en fechas diferentes, cambiar a "available"
        if (!otherDates) {
          await axios.put(
            `http://127.0.0.1:8000/tables/${existingReservation.table_id}`,
            { status: 'available' },
            { headers: { 'Content-Type': 'application/json' } }
          );
          console.log(`Table ${existingReservation.table_id} updated to available.`);
        } else {
          console.log(`Table ${existingReservation.table_id} still has active reservations on other dates. Keeping status as "reserved".`);
        }
      }

      // Cambiar mesas si `tableId` cambia
      if (tableId && tableId !== existingReservation.table_id) {
        // Liberar la mesa anterior si no hay otras reservaciones activas para ella
        const activeReservationsForOldTableQuery = `
          SELECT reservation_date FROM reservations
          WHERE table_id = $1 AND status = 'ACTIVE';
        `;
        const activeReservationsForOldTableResult = await pool.query(activeReservationsForOldTableQuery, [
          existingReservation.table_id,
        ]);

        const otherDatesOldTable = activeReservationsForOldTableResult.rows.some(
          (reservation) => reservation.reservation_date !== existingReservation.reservation_date
        );

        if (!otherDatesOldTable) {
          await axios.put(
            `http://127.0.0.1:8000/tables/${existingReservation.table_id}`,
            { status: 'available' },
            { headers: { 'Content-Type': 'application/json' } }
          );
          console.log(`Old table ${existingReservation.table_id} updated to available.`);
        }


        // Reservar la nueva mesa
        await axios.put(
          `http://127.0.0.1:8000/tables/${tableId}`,
          { status: 'reserved' },
          { headers: { 'Content-Type': 'application/json' } }
        );
        console.log(`Table ${tableId} updated to reserved.`);
      }
    } catch (error) {
      console.error('Error updating table status:', error.message);
      return res.status(500).json({
        message: 'Reservation updated, but failed to update table status',
        reservation: updatedReservation,
        error: 'Error updating table status in tables-management',
      });
    }

    console.log('Reservation updated:', updateResult.rows[0]);
    res.status(200).json({ message: 'Reservation updated', reservation: updateResult.rows[0] });
  } catch (error) {
    console.error('Error updating reservation:', error.message);
    res.status(500).json({ error: 'Error updating reservation', details: error.message });
  }
};

module.exports = modifyReservation;
