const pool = require('../../database/db');
const { hashPassword } = require('../../utils/hashPassword');


module.exports = async (req, res) => {
  const { name, email, password, role } = req.body;

  if (!name || !email || !password) {
    return res.status(400).json({ error: 'Todos los campos son obligatorios' });
  }

  try {
    const hashedPassword = await hashPassword(password);
    const result = await pool.query(
      'INSERT INTO users (name, email, password, role) VALUES ($1, $2, $3, $4) RETURNING id, name, email, role',
      [name, email, hashedPassword, role || 'user']
    );
    res.status(201).json({ message: 'Usuario creado', user: result.rows[0] });
  } catch (error) {
    if (error.code === '23505') {
      res.status(400).json({ error: 'El correo ya está registrado' });
    } else {
      res.status(500).json({ error: 'Error al crear usuario', details: error.message });
    }
  }
};
