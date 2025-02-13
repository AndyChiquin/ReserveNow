const bcrypt = require("bcrypt");
const pool = require("../../database/db"); // Conexión a la base de datos

const registerUser = async (req, res) => {
  const { fullName, email, password } = req.body;

  try {
    // Verificar si el usuario ya existe
    const userExists = await pool.query("SELECT * FROM users WHERE email = $1", [email]);
    if (userExists.rows.length > 0) {
      return res.status(400).json({ message: "El usuario ya existe." });
    }

    // Hashear la contraseña antes de guardarla
    const hashedPassword = await bcrypt.hash(password, 10);

    // Insertar usuario en la base de datos
    await pool.query(
      "INSERT INTO users (name, email, password, role, created_at, updated_at) VALUES ($1, $2, $3, $4, NOW(), NOW())",
      [fullName, email, hashedPassword, "user"]
    );

    res.status(201).json({ message: "Usuario registrado correctamente." });
  } catch (error) {
    console.error("Error en el registro:", error);
    res.status(500).json({ message: "Error interno del servidor." });
  }
};

module.exports = registerUser;
