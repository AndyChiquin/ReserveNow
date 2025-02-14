const bcrypt = require("bcrypt");
const pool = require("../../database/db"); // ✅ SRP: Handles only database connection.

const registerUser = async (req, res) => {
  const { fullName, email, password } = req.body;

  try {
    // ✅ SRP: User existence check is a separate responsibility from user creation.
    const userExists = await pool.query("SELECT * FROM users WHERE email = $1", [email]);
    if (userExists.rows.length > 0) {
      return res.status(400).json({ message: "El usuario ya existe." });
    }

    // ✅ SRP: Password hashing is a separate responsibility handled by bcrypt.
    const hashedPassword = await bcrypt.hash(password, 10);

    // ✅ SRP: Database insertion is a distinct responsibility.
    await pool.query(
      "INSERT INTO users (name, email, password, role, created_at, updated_at) VALUES ($1, $2, $3, $4, NOW(), NOW())",
      [fullName, email, hashedPassword, "user"]
    );

    res.status(201).json({ message: "Usuario registrado correctamente." }); // ✅ SRP: Handles only response sending.

  } catch (error) {
    console.error("Error en el registro:", error); // ✅ SRP: Logging is separate from response handling.
    res.status(500).json({ message: "Error interno del servidor." });
  }
};

module.exports = registerUser; // ✅ SRP: Module exports only the register function.
