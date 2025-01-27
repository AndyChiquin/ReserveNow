const pool = require('../../database/db');
const { comparePassword } = require('../../utils/hashPassword');
const { generateToken } = require('../../utils/jwtManager');

module.exports = async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password are required' });
  }

  try {
    const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
    if (result.rowCount === 0) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const user = result.rows[0];

    const isValidPassword = await comparePassword(password, user.password);
    if (!isValidPassword) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = generateToken({ id: user.id, email: user.email, role: user.role });

    res.status(200).json({ message: 'Successful login', token });
  } catch (error) {
    res.status(500).json({ error: 'Error logging in', details: error.message });
  }
};
