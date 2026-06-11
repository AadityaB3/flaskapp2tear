#!/bin/bash

echo "Applying Kubernetes Resources..."

kubectl apply -f secret.yaml
kubectl apply -f configmap.yaml
kubectl apply -f pvc.yaml
kubectl apply -f databaseservice.yaml
kubectl apply -f databasedeployment.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

echo "Waiting for MySQL Pod..."

sleep 60

MYSQL_POD=$(kubectl get pods -l app=mysql -o jsonpath="{.items[0].metadata.name}")

echo "MySQL Pod: $MYSQL_POD"

kubectl exec -i $MYSQL_POD -- mysql -uroot -proot -e "
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
"

echo "Deployment Completed Successfully"
