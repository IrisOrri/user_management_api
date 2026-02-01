# User Management API 🚀

A secure, production-grade Backend API built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**. This project demonstrates modern backend architecture, focusing on security, scalability, and clean data validation.

## 🛠️ Technical Stack
* **Framework:** FastAPI (Asynchronous Python)
* **Database:** PostgreSQL (Cloud-hosted via Neon/Supabase)
* **ORM:** SQLAlchemy (Object-Relational Mapping)
* **Security:** JWT (JSON Web Tokens) & Bcrypt password hashing
* **Validation:** Pydantic (Strict typing and schemas)

## 🔑 Key Features
* **Full CRUD Lifecycle:** Complete implementation of Create, Read, Update, and Delete operations for user resources.
* **Stateless Auth:** Implements OAuth2 with JWT for secure, scalable user sessions.
* **Granular Security:** Protected routes ensure users can only modify or delete their own profiles.
* **Database Security:** One-way password hashing using the Bcrypt algorithm.
* **Interactive Docs:** Integrated Swagger UI for testing endpoints at `/docs`.



## 📡 API Endpoints

| Method | Endpoint | Access | Description |
| :--- | :--- | :--- | :--- |
| **POST** | `/users/` | Public | **Create**: Register a new user account. |
| **POST** | `/login` | Public | **Login**: Exchange credentials for a JWT Access Token. |
| **GET** | `/users/me` | Private | **Read**: Retrieve current authenticated user profile. |
| **PUT** | `/users/me` | Private | **Update**: Modify email or password for current user. |
| **DELETE**| `/users/me` | Private | **Delete**: Permanently remove the current user account. |

## 📁 Project Structure
* `main.py` - API routing and entry point.
* `auth.py` - JWT logic, password hashing, and dependency injection.
* `models.py` - SQLAlchemy database table definitions.
* `schemas.py` - Pydantic models for request/response validation.
* `database.py` - Session management and engine configuration.

## 🏁 How to Run Locally
1. Clone the repository.
2. Install dependencies: 
   ```powershell
   pip install -r requirements.txt