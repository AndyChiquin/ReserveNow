const pool = require('../../database/db'); // ✅ OCP: Database connection is external, avoiding direct modification.
const { hashPassword } = require('../../utils/hashPassword'); // ✅ OCP: Password hashing is handled externally.

module.exports = async (req, res) => {
  const { id } = req.params;
  const { name, email, password, role } = req.body;

  try {
    // ✅ OCP: Password hashing logic is independent, allowing for easy modification without affecting update logic.
    const hashedPassword = password ? await hashPassword(password) : null;

    // ✅ OCP: The update query is flexible and allows modifications without changing the structure.
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

    // ✅ OCP: The response handling is modular, allowing for extended functionalities in the future.
    if (result.rowCount === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(200).json({ message: 'Updated user', user: result.rows[0] });

  } catch (error) {
    res.status(500).json({ error: 'Error updating user', details: error.message }); // ✅ OCP: Generic error handling that can be extended.
  }
};
