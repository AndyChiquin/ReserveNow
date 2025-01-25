const pool = require('../../database/db');
const { hashPassword } = require('../../utils/hashPassword');

module.exports = async (req, res) => {
  const { id } = req.params;
  const { name, email, password, role } = req.body;

  try {
    const hashedPassword = password ? await hashPassword(password) : null;
    const result = await pool.query(
      `UPDATE users 
       SET name = COALESCE($1, name), 
           email = COALESCE($2, email), 
           password = COALESCE($3, password), 
           role = COALESCE($4, role), 
           updated_at = NOW()
       WHERE id = $5 RETURNING id, name, email, role`,
      [name, email, hashedPassword, role, id]
    );

    if (result.rowCount === 0) {
      return res.status(404).json({ error: 'Usuario no encontrado' });
    }

    res.status(200).json({ message: 'Usuario actualizado', user: result.rows[0] });
  } catch (error) {
    res.status(500).json({ error: 'Error al actualizar usuario', details: error.message });
  }
};
