const express = require('express');
const { blockUser } = require('../controllers/createBlockedController');

const router = express.Router();

router.post('/', blockUser);

module.exports = router;
