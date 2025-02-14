# Reservation Management Service

## Overview
The **Reservation Management Service** is a microservice responsible for handling restaurant reservations. It ensures proper table availability, allows users to create, update, retrieve, and cancel reservations, and integrates with authentication and table management services.

## Features
- **Create reservations** while checking table availability.
- **Retrieve reservations** by ID or list all reservations.
- **Update reservations** (change date, table, or status).
- **Cancel reservations** and release tables.
- **Integration with Authentication & Table Management services**.

## Tech Stack
- **Backend:** Node.js with Express.js
- **Database:** PostgreSQL (Hosted on AWS RDS)
- **Containerization:** Docker & Docker Compose
- **Deployment:** AWS EC2

## Endpoints

| Method   | Endpoint                 | Description                     |
|----------|--------------------------|---------------------------------|
| `POST`   | `/reservations`          | Create a new reservation       |
| `GET`    | `/reservations`          | Retrieve all reservations      |
| `GET`    | `/reservations/{id}`     | Get reservation by ID          |
| `PUT`    | `/reservations/{id}`     | Update a reservation           |
| `DELETE` | `/reservations/{id}`     | Cancel a reservation           |

