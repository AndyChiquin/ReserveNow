<?php
require_once '../../db/database.php';

function getBlockedUser($id) {
    $db = new Database();
    $stmt = $db->conn->prepare("SELECT * FROM blocked_users WHERE id = ?");
    $stmt->execute([$id]);
    return $stmt->fetch(PDO::FETCH_ASSOC);
}
?>
