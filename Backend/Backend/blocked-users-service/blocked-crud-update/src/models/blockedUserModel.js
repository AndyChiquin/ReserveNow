const { DataTypes } = require('sequelize');
const sequelize = require('../config/db');

const BlockedUser = sequelize.define('BlockedUser', {
  userId: {
    type: DataTypes.INTEGER,
    allowNull: false,
    unique: true
  },
  reason: {
    type: DataTypes.STRING,
    allowNull: false
  }
}, {
  timestamps: true  // Esto agrega automáticamente `createdAt` y `updatedAt`
});

module.exports = BlockedUser;
