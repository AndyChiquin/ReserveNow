<?php
header("Content-Type: application/json");

echo json_encode([
    "message" => "Blocked-Users Service is running",
    "endpoints" => [
        "POST /api/create/route.php" => "Block a user",
        "GET /api/read/route.php?id={id}" => "Get a blocked user",
        "DELETE /api/delete/route.php?id={id}" => "Unblock a user"
    ]
]);
?>
