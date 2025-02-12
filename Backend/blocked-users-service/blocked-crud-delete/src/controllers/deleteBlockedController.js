const BlockedUser = require('../models/blockedUserModel');

const unblockUser = async (req, res) => {
  const { userId } = req.params;

  try {
    console.log(`🗑️ Eliminando usuario bloqueado con userId: ${userId}`);

    const deleted = await BlockedUser.destroy({ where: { userId } });

    if (!deleted) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.status(200).json({ message: 'User unblocked successfully' });
  } catch (error) {
    console.error(`❌ Error al eliminar usuario bloqueado: ${error.message}`);
    res.status(500).json({ error: 'Failed to unblock user' });
  }
};

module.exports = { unblockUser };
