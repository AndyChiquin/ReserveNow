const pool = require('../../database/db');

module.exports = async (req, res) => {
  const { id } = req.params;

  try {
    const result = await pool.query('SELECT id, name, email, role FROM users WHERE id = $1', [id]);

    if (result.rowCount === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(200).json(result.rows[0]);
  } catch (error) {
    res.status(500).json({ error: 'Error getting user', details: error.message });
  }
};
