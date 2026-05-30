CREATE DATABASE IF NOT EXISTS receipt_db;
USE receipt_db;

CREATE TABLE receipts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    payer VARCHAR(100),
    language VARCHAR(50),
    items TEXT,
    total FLOAT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

