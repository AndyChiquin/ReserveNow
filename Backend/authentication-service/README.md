# 🛡️ Authentication Service - ReserveNow

This microservice is part of the **ReserveNow** ecosystem and handles user authentication and management.

## 🚀 Technologies Used.
- **Language**: Node.js (JavaScript)
- **Framework**: Express.js
- Database**: PostgreSQL (AWS RDS)
- Dependency Management**: npm
- Containers**: Docker & Docker Compose
- Cloud Orchestration**: AWS EC2
- Security**: JWT for authentication (under development)
- **Communication**: REST API

## 📌 Available Endpoints.

### 🔹 `GET /auth/users`.
Gets the list of registered users.

### 🔹 `POST /auth/register`
Registers a new user in the system.  
**Body (JSON):**
```json
{
  “name": ‘Juan Perez’,
  “email": ‘juan.perez@example.com’,
  “password": ‘123456’,
  “role": ”user”
}

