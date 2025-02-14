# Special Days Microservice 🎉

This microservice is responsible for managing **special days** in a **restaurant reservation system**. It allows users to **create, read, update, and delete (CRUD)** special days stored in a **PostgreSQL database hosted on AWS RDS**.

## 🚀 Features
- ✅ **Create** a new special day (`POST /create`)
- ✅ **Retrieve** all special days (`GET /read`)
- ✅ **Retrieve** a special day by ID (`GET /read/{id}`)
- ✅ **Update** a special day (`PUT /update/{id}`)
- ✅ **Delete** a special day (`DELETE /delete/{id}`)

## 🛠️ Technologies Used
- **Python 3.10** 🐍
- **Flask** (for API development)
- **PostgreSQL** (hosted on AWS RDS)
- **SQLAlchemy** (ORM for database interaction)
- **Flask-Migrate** (for database migrations)
- **Docker** (for containerized deployment)
- **AWS EC2** (for cloud deployment)

## 📦 Project Structure
