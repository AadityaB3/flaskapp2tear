CREATE DATABASE notesdb;

USE notesdb;

CREATE TABLE notes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL
);

INSERT INTO notes(content)
VALUES('Welcome To My Notes App');