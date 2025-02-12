const express = require('express');
const { isUserBlocked } = require('../controllers/readBlockedController');

const router = express.Router();

router.get('/:userId', isUserBlocked);

module.exports = router;
