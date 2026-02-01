# User Management API 🚀

A secure, production-grade Backend API built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**. This project demonstrates modern backend architecture, focusing on security, scalability, and clean data validation.



## 🛠️ Technical Stack
* **Framework:** FastAPI (Asynchronous Python)
* **Database:** PostgreSQL (Cloud-hosted via Neon/Supabase)
* **ORM:** SQLAlchemy (Object-Relational Mapping)
* **Security:** JWT (JSON Web Tokens) & Bcrypt password hashing
* **Validation:** Pydantic (Strict typing and schemas)

## 🔑 Key Features
* **Stateless Auth:** Implements OAuth2 with JWT for secure, scalable user sessions.
* **Database Security:** One-way password hashing using the Bcrypt algorithm.
* **Automated Logic:** Uses SQLAlchemy `Base.metadata` for automated table creation.
* **Interactive Docs:** Integrated Swagger UI for testing endpoints at `/docs`.

## 📁 Project Structure
* `main.py` - API routing and entry point.
* `auth.py` - Hashing logic and JWT generation.
* `models.py` - Database table definitions.
* `schemas.py` - Pydantic models for data validation.
* `database.py` - Connection and session management.

## 🏁 How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your `DATABASE_URL` and `SECRET_KEY`.
4. Start the server: `uvicorn main:app --reload`
