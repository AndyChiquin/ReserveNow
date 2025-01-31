<?php
require_once '../../db/database.php';

function deleteBlockedUser($id) {
    $db = new Database();
    $stmt = $db->conn->prepare("DELETE FROM blocked_users WHERE id = ?");
    
    try {
        $stmt->execute([$id]);
        return ["message" => "User deleted successfully"];
    } catch (PDOException $e) {
        return ["error" => "Error deleting user"];
    }
}
?>
