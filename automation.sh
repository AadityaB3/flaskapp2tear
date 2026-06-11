#!/bin/bash

echo "Starting Docker Compose..."

docker compose up -d

echo "Waiting for MySQL to start..."

sleep 30

echo "Creating Database and Table..."

docker exec -i mysql-db mysql -uroot -proot -e "
CREATE DATABASE IF NOT EXISTS notesdb;

USE notesdb;

CREATE TABLE IF NOT EXISTS notes (
id INT AUTO_INCREMENT PRIMARY KEY,
content TEXT NOT NULL
);

INSERT INTO notes(content)
SELECT 'Welcome To My Notes App'
WHERE NOT EXISTS (
SELECT * FROM notes
WHERE content='Welcome To My Notes App'
);
"

echo "Database setup completed."

echo "Application URL:"
echo "http://<EC2-PUBLIC-IP>:5000"
