const pool = require('../../database/db'); // ✅ KISS: Simple import for database connection.

module.exports = async (req, res) => {
  const { id } = req.params; // ✅ KISS: Extracts user ID from request parameters.

  try {
    // ✅ KISS: Simple, clear SQL query to delete a user.
    const result = await pool.query('DELETE FROM users WHERE id = $1 RETURNING *', [id]);

    // ✅ KISS: Early return avoids unnecessary nesting.
    if (result.rowCount === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(200).json({ message: 'User deleted', user: result.rows[0] }); // ✅ KISS: Clear success response.

  } catch (error) {
    res.status(500).json({ error: 'Error deleting user', details: error.message }); // ✅ KISS: Straightforward error handling.
  }
};
