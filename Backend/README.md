# ReserveNow - Backend

This repository contains the backend of the **ReserveNow** system, a reservation management system for restaurants based on a microservices architecture.

## 📌 Description.

The backend of **ReserveNow** is composed of multiple microservices that manage different aspects of the system, such as user authentication, reservation management, tables, schedules, employees and reports. Each microservice is developed with specific technologies and communicates through REST APIs.

## 🏗️ Architecture

The backend follows an architecture based on **microservices**, where each service is independent and can be scaled individually. Communication between microservices is done via HTTP and database connections in **AWS RDS**.

### Microservices and Technologies
In each microservice the architecture of each microservice is better detailed.

## 🚀 Deployment on AWS.

The backend is deployed on **AWS**, using:

- **EC2** to host the microservices.
- **AWS RDS** for the databases
- Docker** for containerization of microservices

### 🏗️ Deployment steps