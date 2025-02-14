# Employees Service

## Overview
The **Employees Service** is a microservice for managing employee data within the **ReserveNow** system. It provides CRUD operations and validates employee associations with restaurants. The service uses **Redis** for fast data storage and retrieval.

## Features
- Create, read, update, and delete employees.
- Ensures that employees are linked to a valid restaurant.
- Uses **Redis** as an in-memory data store.
- Containerized with **Docker** for easy deployment.

## Technologies Used
- **Python 3.10**
- **Flask**
- **Redis**
- **Docker & Docker Compose**
- **AWS EC2**

## API Endpoints
- `POST /employees` → Create a new employee.
- `GET /employees` → Retrieve all employees.
- `GET /employees/{employee_id}` → Get a specific employee.
- `PUT /employees/{employee_id}` → Update employee data.
- `DELETE /employees/{employee_id}` → Remove an employee.



