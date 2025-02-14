
# 🍽️ Restaurants Service  

## 📌 Description  
This microservice manages restaurant operations, allowing users to create, read, update, and deactivate restaurants. It is built using Python and Flask, with a MariaDB database for data storage, and runs as containerized services using Docker and Docker Compose.

---

## 🛠️ Technologies Used  
- **Programming Language:** Python 3.10  
- **Framework:** Flask  
- **Database:** MariaDB (AWS RDS)  
- **Containerization:** Docker & Docker Compose  
- **Deployment:** AWS EC2  

---

## 🚀 Endpoints  

| Method | Endpoint                     | Description                     |
|--------|------------------------------|---------------------------------|
| POST   | `/restaurants`               | Create a new restaurant        |
| GET    | `/restaurants`               | Retrieve all restaurants       |
| GET    | `/restaurants/{id}`          | Retrieve a restaurant by ID    |
| PUT    | `/restaurants/{id}/status`   | Update the status of a restaurant |
| DELETE | `/restaurants/{id}`          | Deactivate a restaurant        |

---
