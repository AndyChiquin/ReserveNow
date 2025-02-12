const axios = require('axios');
const BlockedUser = require('../models/blockedUserModel');

const userExists = async (userId) => {
  try {
    const url = `${process.env.USERS_READ_SERVICE_URL}/api/users/${userId}`;
    console.log(`🔍 Verificando usuario en: ${url}`);

    const response = await axios.get(url);
    return response.status === 200;
  } catch (error) {
    console.error(`❌ Error al conectar con users-service: ${error.message}`);
    return false;
  }
};

const blockUser = async (req, res) => {
  const { userId, reason } = req.body;

  if (!userId || !reason) {
    return res.status(400).json({ error: 'Missing userId or reason' });
  }

  if (!(await userExists(userId))) {
    return res.status(404).json({ error: 'User not found in users-service' });
  }

  try {
    const blockedUser = await BlockedUser.create({ userId, reason });
    res.status(201).json({ message: 'User blocked successfully', data: blockedUser });
  } catch (error) {
    res.status(500).json({ error: 'Failed to block user' });
  }
};

module.exports = { blockUser };
