# Feedbacks Service

This microservice handles user feedback submissions for restaurants. It allows users to create, read, update, and delete feedback entries while ensuring data consistency by validating users and reservations.

## Features
- **Create Feedback:** Users can submit feedback with a rating and comment.
- **Read Feedbacks:** Retrieve all stored feedback entries.
- **Update Feedback:** Modify an existing feedback entry.
- **Delete Feedback:** Remove feedback entries from the database.
- **Validation:** Checks if users, reservations, and restaurants exist before processing requests.

## Technologies Used
- **Python 3.9**
- **Flask** (for API development)
- **Microsoft SQL Server** (as the database)
- **Docker & Docker Compose** (for containerization)
- **PyODBC** (for database connection)


