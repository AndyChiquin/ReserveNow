<?php
require_once '../db/database.php';

header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = json_decode(file_get_contents("php://input"), true);

    if (!isset($data["id"]) || !isset($data["email"]) || !isset($data["reason"])) {
        http_response_code(400);
        echo json_encode(["error" => "Missing required fields"]);
        exit();
    }

    $db = new Database();
    $stmt = $db->conn->prepare("INSERT INTO blocked_users (id, email, reason, blocked_at) VALUES (?, ?, ?, ?)");
    
    try {
        $stmt->execute([$data["id"], $data["email"], $data["reason"], date("Y-m-d H:i:s")]);
        echo json_encode(["message" => "User blocked successfully"]);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Error blocking user"]);
    }
}
?>
<?php
require_once '../db/database.php';

header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = json_decode(file_get_contents("php://input"), true);

    if (!isset($data["id"]) || !isset($data["email"]) || !isset($data["reason"])) {
        http_response_code(400);
        echo json_encode(["error" => "Missing required fields"]);
        exit();
    }

    $db = new Database();
    $stmt = $db->conn->prepare("INSERT INTO blocked_users (id, email, reason, blocked_at) VALUES (?, ?, ?, ?)");
    
    try {
        $stmt->execute([$data["id"], $data["email"], $data["reason"], date("Y-m-d H:i:s")]);
        echo json_encode(["message" => "User blocked successfully"]);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Error blocking user"]);
    }
}
?>
