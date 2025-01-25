const pool = require('../../database/db');

module.exports = async (req, res) => {
  try {
    const result = await pool.query('SELECT id, name, email, role FROM users');
    res.status(200).json(result.rows);
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener usuarios', details: error.message });
  }
};
