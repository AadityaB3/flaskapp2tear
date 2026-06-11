import subprocess
import time

files = [
"secret.yaml",
"configmap.yaml",
"pvc.yaml",
"databaseservice.yaml",
"databasedeployment.yaml",
"deployment.yaml",
"service.yaml"
]

print("Applying Kubernetes Resources...")

for file in files:
subprocess.run(
["kubectl", "apply", "-f", file],
check=True
)

print("Waiting for MySQL Pod...")

time.sleep(60)

pod = subprocess.check_output(
[
"kubectl",
"get",
"pods",
"-l",
"app=mysql",
"-o",
"jsonpath={.items[0].metadata.name}"
]
).decode().strip()

print("MySQL Pod:", pod)

sql = """
CREATE DATABASE IF NOT EXISTS notesdb;

USE notesdb;

CREATE TABLE IF NOT EXISTS notes(
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

subprocess.run(
[
"kubectl",
"exec",
"-i",
pod,
"--",
"mysql",
"-uroot",
"-proot",
"-e",
sql
],
check=True
)

print("Deployment Completed Successfully")

