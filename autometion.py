import subprocess
import time

print("Starting Docker Compose...")

subprocess.run(
["docker", "compose", "up", "-d"],
check=True
)

print("Waiting for MySQL to start...")

time.sleep(30)

sql_query = """
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
"""

print("Creating Database and Table...")

subprocess.run(
[
"docker",
"exec",
"-i",
"mysql-db",
"mysql",
"-uroot",
"-proot",
"-e",
sql_query
],
check=True
)

print("Deployment Completed Successfully")
print("Access Application:")
print("http://<EC2-PUBLIC-IP>:5000")
