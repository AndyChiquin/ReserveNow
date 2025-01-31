<?php
require_once 'service.php';

header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] == "DELETE" && isset($_GET["id"])) {
    echo json_encode(deleteBlockedUser($_GET["id"]));
}
?>
