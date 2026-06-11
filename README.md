# Flask Notes App

Features:

- Add Notes
- Delete Notes
- MySQL Database
- Docker Multi-stage Build
- Attractive UI

Run:

docker build -t notes-app:v1 .

docker run -d -p 5000:5000 notes-app:v1

Docker Compose:

docker compose up --build

Kubernetes:

For a local Kubernetes cluster, build the image first:

docker build -t notes-app:v1 .

kubectl apply -f secret.yaml

kubectl apply -f configmap.yaml

kubectl apply -f pvc.yaml

kubectl apply -f databaseservice.yaml

kubectl apply -f databasedeployment.yaml

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

Or run:

python k8s.py

For a remote cluster, push the image to a registry and update deployment.yaml image name.
