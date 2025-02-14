const pool = require('../../database/db'); // ✅ SRP: Handles database connection only.
const { hashPassword } = require('../../utils/hashPassword'); // ✅ SRP: Handles password hashing only.

module.exports = async (req, res) => {
  const { name, email, password, role } = req.body;

  // ✅ SRP: This block handles only input validation.
  if (!name || !email || !password) {
    return res.status(400).json({ error: 'All fields are required' });
  }

  try {
    const hashedPassword = await hashPassword(password); // ✅ SRP: Hashing logic is delegated to another module.
    
    // ✅ SRP: This query is responsible for inserting a new user.
    const result = await pool.query(
      'INSERT INTO users (name, email, password, role) VALUES ($1, $2, $3, $4) RETURNING id, name, email, role',
      [name, email, hashedPassword, role || 'user']
    );

    res.status(201).json({ message: 'User created', user: result.rows[0] }); // ✅ SRP: Responsible for sending a success response.

  } catch (error) {
    // ✅ SRP: Error handling block.
    if (error.code === '23505') {
      res.status(400).json({ error: 'The email is already registered' }); // Handles duplicate email error.
    } else {
      res.status(500).json({ error: 'Error creating user', details: error.message }); // Handles other database errors.
    }
  }
};
