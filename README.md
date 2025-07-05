# 📝 Task Management API

A RESTful API for managing tasks, built with Django, Django REST Framework, and JWT authentication.

---

## 🚀 Features

- User registration and login (JWT)
- Create, retrieve, update, and delete tasks
- Authenticated access per user
- Swagger UI documentation

---

## 🧰 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- Simple JWT
- drf-yasg (Swagger UI)

---

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

📬 API Endpoints
| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| POST   | `/api/users/register/` | User registration |
| POST   | `/api/users/token/`    | Obtain JWT token  |
| GET    | `/api/tasks/`          | List tasks        |
| POST   | `/api/tasks/`          | Create task       |
| GET    | `/api/tasks/<id>/`     | Retrieve task     |
| PUT    | `/api/tasks/<id>/`     | Update task       |
| DELETE | `/api/tasks/<id>/`     | Delete task       |
