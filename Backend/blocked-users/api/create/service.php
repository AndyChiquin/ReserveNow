<?php
require_once '../../db/database.php';

function blockUser($id, $email, $reason) {
    $db = new Database();
    $stmt = $db->conn->prepare("INSERT INTO blocked_users (id, email, reason, blocked_at) VALUES (?, ?, ?, ?)");
    
    try {
        $stmt->execute([$id, $email, $reason, date("Y-m-d H:i:s")]);
        return ["message" => "User blocked successfully"];
    } catch (PDOException $e) {
        return ["error" => "Error blocking user"];
    }
}
?>
