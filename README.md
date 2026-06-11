# Flask Notes App

Features:

- Add Notes
- Delete Notes
- MySQL Database
- Docker Multi-stage Build
- Attractive UI

Run:

docker build -f Dockerfile-multistage -t notes-app:v1 .

docker run -d -p 5000:5000 notes-app:v1

tablle manually add karycha

kubectl apply -f secret.yaml

kubectl apply -f configmap.yaml

kubectl apply -f pvc.yaml

kubectl apply -f databaseservice.yaml

kubectl apply -f databasedeployment.yaml

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml