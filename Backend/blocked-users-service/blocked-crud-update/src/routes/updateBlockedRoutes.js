const express = require('express');
const { updateBlockedUser } = require('../controllers/updateBlockedController');

const router = express.Router();

router.put('/:userId', updateBlockedUser);

module.exports = router;
