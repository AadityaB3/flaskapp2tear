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