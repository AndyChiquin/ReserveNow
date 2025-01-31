<?php
require_once __DIR__ . '/../vendor/autoload.php'; // Cargar dotenv

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__ . '/../');
$dotenv->load();

class Database {
    private $db_file;
    public $conn;

    public function __construct() {
        $host = $_ENV["DB_HOST"] ?? getenv("DB_HOST");
        $port = $_ENV["DB_PORT"] ?? getenv("DB_PORT");
        $db_path = $_ENV["DB_NAME"] ?? getenv("DB_NAME");

        // Si se define un host y puerto, conectamos a la base de datos en EC2
        if ($host && $port) {
            $this->db_file = "tcp:$host:$port";
        } else {
            $this->db_file = $db_path; // Local SQLite
        }

        try {
            $this->conn = new PDO("sqlite:" . $this->db_file);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            die("Database connection failed: " . $e->getMessage());
        }
    }
}
?>

