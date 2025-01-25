const pool = require('../../database/db');

module.exports = async (req, res) => {
  const { id } = req.params;

  try {
    const result = await pool.query('DELETE FROM users WHERE id = $1 RETURNING *', [id]);

    if (result.rowCount === 0) {
      return res.status(404).json({ error: 'Usuario no encontrado' });
    }

    res.status(200).json({ message: 'Usuario eliminado', user: result.rows[0] });
  } catch (error) {
    res.status(500).json({ error: 'Error al eliminar usuario', details: error.message });
  }
};
