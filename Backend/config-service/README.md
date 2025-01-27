# Config Service

## Overview
The **Config Service** is a microservice built with FastAPI that manages global configurations for a system. It provides APIs to create, read, and delete configurations stored in a MySQL database hosted on AWS RDS.

---

## Features
- **Create Configurations**: Add new configuration key-value pairs.
- **Read Configurations**: Retrieve stored configurations by their keys.
- **Delete Configurations**: Remove existing configurations from the database.

---

## Endpoints
| Method | Endpoint            | Description                  |
|--------|---------------------|------------------------------|
| POST   | `/create/configs/`  | Create a new configuration.  |
| GET    | `/read/configs/{key}` | Retrieve a configuration by its key. |
| DELETE | `/delete/configs/{key}` | Delete a configuration by its key. |

---

## Requirements
- Python 3.9 or higher
- MySQL database (hosted on AWS RDS or locally)

---

## Environment Variables
The application requires the following environment variables to function:
```plaintext
DATABASE_URL=mysql+pymysql://<username>:<password>@<host>:<port>/<database>
