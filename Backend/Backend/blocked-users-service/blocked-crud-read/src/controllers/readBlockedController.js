const BlockedUser = require('../models/blockedUserModel');

const isUserBlocked = async (req, res) => {
  const { userId } = req.params;

  try {
    console.log(`🔍 Buscando usuario bloqueado con userId: ${userId}`);
    
    const blockedUser = await BlockedUser.findOne({ where: { userId } });

    if (!blockedUser) {
      return res.status(404).json({ message: 'User is not blocked' });
    }

    res.status(200).json(blockedUser);
  } catch (error) {
    console.error(`❌ Error al consultar usuario bloqueado: ${error.message}`);
    res.status(500).json({ error: 'Failed to check blocked user' });
  }
};

module.exports = { isUserBlocked };
