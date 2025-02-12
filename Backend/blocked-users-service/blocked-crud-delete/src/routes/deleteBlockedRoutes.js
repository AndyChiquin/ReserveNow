const express = require('express');
const { unblockUser } = require('../controllers/deleteBlockedController');

const router = express.Router();

router.delete('/:userId', unblockUser);

module.exports = router;
