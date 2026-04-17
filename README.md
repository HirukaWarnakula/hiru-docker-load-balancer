# Nginx Load Balancer with Docker Compose 🚀⚖️

This project demonstrates how to scale a web application and distribute traffic using an **Nginx Load Balancer**. It uses a **Round-Robin** algorithm to redirect incoming requests across multiple Python (Flask) containers.

## 🛠️ Tech Stack
- **Load Balancer:** Nginx
- **Backend:** Python (Flask)
- **Containerization:** Docker & Docker Compose
- **Orchestration:** Manual Scaling (`--scale`)

## 🏗️ Architecture
- **Nginx Container:** Acts as a Reverse Proxy and Load Balancer listening on port 8080.
- **Flask Containers:** Three identical instances of the backend app running simultaneously.

- **Load Balancer(Nginx):** Configured as a reverse proxy that uses the Round-Robin algorithm to distribute incoming traffic on port 8080.

- **Scalable Backend (Flask):** Utilizes Docker's --scale feature to run multiple instances of the application, ensuring that the system remains functional even if one container fails (Self-Healing concept).

- **Internal Networking:** All containers communicate via a dedicated Docker bridge network, keeping the backend isolated from direct public access.



## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/HirukaWarnakula/hiru-docker-load-balancer.git](https://github.com/HirukaWarnakula/hiru-docker-load-balancer.git)

2. Launch the scaled stack:

Bash
docker-compose up --build -d --scale my-app=3

3. Access via: http://localhost:8080
(Refresh the page to see the Container ID change!)

![Preview](preview.jpeg)

Developed by Hiruka Warnakula - Aspiring DevOps Engineer.
