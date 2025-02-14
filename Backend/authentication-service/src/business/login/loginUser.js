const pool = require('../../database/db'); // ✅ DRY: Reusing the database connection module.
const { comparePassword } = require('../../utils/hashPassword'); // ✅ DRY: Reusing the password comparison function.
const { generateToken } = require('../../utils/jwtManager'); // ✅ DRY: Reusing token generation function.

module.exports = async (req, res) => {
  const { email, password } = req.body;

  // ✅ DRY: Centralized validation check to avoid repeating similar checks later.
  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password are required' });
  }

  try {
    const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);

    // ✅ DRY: Unified error message for invalid credentials, avoiding duplicate responses.
    if (result.rowCount === 0 || !(await comparePassword(password, result.rows[0].password))) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const user = result.rows[0];

    // ✅ DRY: Token generation logic is reused through a utility function.
    const token = generateToken({ id: user.id, email: user.email, role: user.role });

    res.status(200).json({ message: 'Successful login', token });

  } catch (error) {
    res.status(500).json({ error: 'Error logging in', details: error.message }); // ✅ DRY: Centralized error handling.
  }
};
