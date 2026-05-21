# Flask + Node.js Dockerized Application

This project demonstrates a multi-container application using:

- Frontend: Node.js with Express
- Backend: Flask (Python)
- Containerization: Docker
- Orchestration: Docker Compose

The frontend sends form data to the Flask backend, and both services run inside the same Docker network.

---

## 📁 Project Structure

```
flask-node-app/
│
├── frontend/
│   ├── app.js
│   ├── package.json
│   ├── Dockerfile
│   └── views/
│       └── index.ejs
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml
