const pool = require('../../database/db'); // ✅ YAGNI: Only importing necessary dependencies.

module.exports = async (req, res) => {
  const { id } = req.params;

  try {
    // ✅ YAGNI: The query retrieves only the required fields, avoiding unnecessary data.
    const result = await pool.query('SELECT id, name, email, role FROM users WHERE id = $1', [id]);

    // ✅ YAGNI: No additional processing is done if the user is not found.
    if (result.rowCount === 0) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(200).json(result.rows[0]); // ✅ YAGNI: Returns only the essential user information.

  } catch (error) {
    res.status(500).json({ error: 'Error getting user', details: error.message }); // ✅ YAGNI: Simple error handling without unnecessary complexity.
  }
};
