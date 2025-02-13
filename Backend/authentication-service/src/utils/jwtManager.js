const jwt = require("jsonwebtoken");
require("dotenv").config(); // Aseguramos que cargue las variables de entorno

const generateToken = (user) => {
  if (!process.env.JWT_SECRET) {
    throw new Error("JWT_SECRET no está definido en el .env");
  }
  return jwt.sign(
    { id: user.id, email: user.email, role: user.role },
    process.env.JWT_SECRET,
    { expiresIn: "1h" }
  );
};

module.exports = { generateToken };
