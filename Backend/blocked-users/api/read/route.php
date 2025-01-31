<?php
require_once 'service.php';

header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["id"])) {
    $user = getBlockedUser($_GET["id"]);
    if ($user) {
        echo json_encode($user);
    } else {
        http_response_code(404);
        echo json_encode(["error" => "User not found"]);
    }
}
?>
