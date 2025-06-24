# 🌙 Late Show API Challenge

**Author:** Eliu Rotich

A robust Flask REST API for managing a Late Night TV show system, built with best practices: MVC architecture, PostgreSQL, JWT authentication, and full Postman test coverage.

---

## 🚀 Features
- Clean MVC folder structure
- PostgreSQL database (no SQLite!)
- Token-based authentication (JWT)
- Secure password hashing
- Cascade delete for appearances
- RESTful endpoints for users, guests, episodes, and appearances
- Postman collection for easy API testing

---

## 🗂 Folder Structure
```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

---

## 🛠 Setup Instructions

### 1. Clone & Install
```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary flask-cors
pipenv shell
```

### 2. PostgreSQL Database
- Create your database:
  ```sql
  CREATE DATABASE late_show_db;
  ```
- Set your `SQLALCHEMY_DATABASE_URI` in `server/config.py`:
  ```python
  SQLALCHEMY_DATABASE_URI = "postgresql://postgres:empire@localhost:5432/late_show_db"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = "your_secret_key"
  JWT_SECRET_KEY = "your_jwt_secret_key"
  ```

### 3. Database Migration & Seeding
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python -m server.seed
```

### 4. Run the Server
```bash
flask --app server.app run
```

---

## 🔐 Auth Flow
- Register: `POST /auth/register` (username, password)
- Login: `POST /auth/login` (username, password) → returns JWT token
- Use JWT: Add header `Authorization: Bearer <token>` to protected requests

---

## 🛣️ API Routes

| Route                        | Method | Auth? | Description                        |
|------------------------------|--------|-------|------------------------------------|
| `/auth/register`             | POST   | ❌    | Register a new user                |
| `/auth/login`                | POST   | ❌    | Log in, get JWT token              |
| `/episodes/`                 | GET    | ❌    | List all episodes                  |
| `/episodes/<id>`             | GET    | ❌    | Get episode + appearances          |
| `/episodes/<id>`             | DELETE | ✅    | Delete episode + appearances       |
| `/guests/`                   | GET    | ❌    | List all guests                    |
| `/appearances/`              | GET    | ❌    | List all appearances               |
| `/appearances/`              | POST   | ✅    | Create an appearance               |

### Sample: Register
```json
POST /auth/register
{
  "username": "alice",
  "password": "password123"
}
```

### Sample: Login
```json
POST /auth/login
{
  "username": "alice",
  "password": "password123"
}
// Response: { "access_token": "..." }
```

### Sample: Create Appearance (JWT required)
```json
POST /appearances/
Headers: { "Authorization": "Bearer <token>" }
{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 2
}
```

---

## 🧪 Postman Usage
- Import `challenge-4-lateshow.postman_collection.json` into Postman.
- Use the provided requests to test all endpoints.
- For protected routes, log in and set the JWT token in the `Authorization` header.

---

## 📝 Notes
- All passwords are securely hashed.
- All protected routes require a valid JWT token.
- Deleting an episode also deletes its appearances (cascade).
- All data is stored in PostgreSQL.

---

## 📎 GitHub Repo
[Your GitHub Repo Link Here]

---

## ✅ Submission Checklist
- [x] MVC folder structure
- [x] PostgreSQL used (no SQLite)
- [x] Models + validations complete
- [x] Auth implemented + protected routes
- [x] Seed data works
- [x] All routes work and tested in Postman
- [x] Clean, complete README.md
- [x] GitHub repo pushed

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
