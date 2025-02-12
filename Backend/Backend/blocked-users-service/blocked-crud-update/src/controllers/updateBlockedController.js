const BlockedUser = require('../models/blockedUserModel');

const updateBlockedUser = async (req, res) => {
  const { userId } = req.params;
  const { reason } = req.body;

  if (!reason) {
    return res.status(400).json({ error: 'Reason is required' });
  }

  try {
    console.log(`🔄 Actualizando motivo de bloqueo para userId: ${userId}`);

    const updated = await BlockedUser.update(
      { reason },
      { where: { userId } }
    );

    if (!updated[0]) {
      return res.status(404).json({ error: 'User not found or no changes made' });
    }

    res.status(200).json({ message: 'Blocked user updated successfully' });
  } catch (error) {
    console.error(`❌ Error al actualizar usuario bloqueado: ${error.message}`);
    res.status(500).json({ error: 'Failed to update blocked user' });
  }
};

module.exports = { updateBlockedUser };
