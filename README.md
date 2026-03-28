# 🚀 Full Stack Boilerplate (Dockerized)

A production-style full-stack boilerplate using:

* Node.js (Backend API)
* React (Frontend)
* PHP (Apache)
* PostgreSQL
* MongoDB
* Redis
* Nginx (Reverse Proxy)
* Docker & Docker Compose

---

## 📦 Tech Stack

* **Backend**: Node.js
* **Frontend**: React
* **PHP Server**: Apache (PHP 8.2)
* **Databases**: PostgreSQL, MongoDB
* **Cache**: Redis
* **Proxy**: Nginx
* **Containerization**: Docker

---

## 🏗️ Project Structure

```
project/
 ├── backend-node/
 ├── frontend-react/
 ├── php-app/
 ├── nginx/
 │    └── default.conf
 ├── docker-compose.yml
 └── .env
```

---

## ⚙️ Prerequisites

Make sure you have installed:

* Docker Desktop
* Node.js (optional for local dev)

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone <your-repo-url>
cd <project-folder>
```

---

### 2. Start all services

```
docker compose up -d
```

---

### 3. Verify running containers

```
docker ps
```

---

## 🌐 Application URLs

| Service            | URL                   |
| ------------------ | --------------------- |
| Nginx (Main Entry) | http://localhost:8080 |
| React App          | http://localhost:3000 |
| Node API           | http://localhost:5001 |
| PHP App            | http://localhost:8081 |

---

## 🧪 Database Connections (Local Tools)

### PostgreSQL

* Host: localhost
* Port: 5432
* User: dev
* Password: dev
* Database: app_db

### MongoDB

```
mongodb://localhost:27017
```

### Redis

* Host: localhost
* Port: 6379

---

## 🔄 Common Commands

### Start services

```
docker compose up -d
```

### Stop services

```
docker compose down
```

### Restart services

```
docker compose restart
```

### View logs

```
docker compose logs -f
```

---

## 🧠 Notes

* Services communicate internally using Docker service names:

  * `postgres`, `mongo`, `redis`
* External tools should use `localhost`
* Nginx acts as a reverse proxy for routing

---

## ⚠️ Troubleshooting

### Port already in use

```
kill -9 $(lsof -ti :PORT)
```

### Reset containers & volumes

```
docker compose down -v
docker compose up -d
```

---

## 🚀 Future Improvements

* Add authentication (JWT)
* Add API structure (routes/controllers)
* Add CI/CD pipeline
* Deploy to AWS / Cloud

---
