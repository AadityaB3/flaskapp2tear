CREATE DATABASE IF NOT EXISTS notesdb;

USE notesdb;

CREATE TABLE IF NOT EXISTS notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL
);

INSERT INTO notes(content)
VALUES('Welcome To My Notes App');
