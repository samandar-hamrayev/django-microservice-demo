Albatta! Quyidagi `README.md` fayli sizning `django-microservice-demo` GitHub loyihangiz uchun to‘liq va professional tarzda yozilgan markdown ko‘rinishidir:

---

````markdown
# Django Microservice Demo

A simple microservices-based demo application using **Django** and **Django REST Framework**, demonstrating a basic architecture with separated **User Service** and **Task Service** communicating via HTTP.

## 📦 Overview

This project is split into two services:

- **User Service**: Handles user data (name, email) with full CRUD capabilities.
- **Task Service**: Handles task data (title, description, user_id) with full CRUD support.
- **API Gateway (proxy endpoint)**: Aggregates user data with related tasks via REST call chaining.

## 🧰 Technologies Used

- Python 3.8+
- Django 4.x
- Django REST Framework
- SQLite (default)
- Requests (used for service-to-service HTTP calls)
- Postman (for API testing)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/samandar-hamrayev/django-microservice-demo.git
cd django-microservice-demo
````

---

### 2. Install and Run User Service

```bash
cd user_service
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt  # Or manually: pip install django djangorestframework requests
python manage.py migrate
python manage.py runserver 8000
```

---

### 3. Install and Run Task Service

In a new terminal:

```bash
cd task_service
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt  # Or manually: pip install django djangorestframework
python manage.py migrate
python manage.py runserver 8001
```

---

## 🚀 API Endpoints

### 📍 User Service ([http://localhost:8000](http://localhost:8000))

* `GET /api/users/` – List users
* `POST /api/users/` – Create user
* `GET /api/users/{id}/` – Retrieve user
* `PUT /api/users/{id}/` – Update user
* `DELETE /api/users/{id}/` – Delete user

### 📍 Task Service ([http://localhost:8001](http://localhost:8001))

* `GET /api/tasks/` – List tasks (optional: `?user_id=1`)
* `POST /api/tasks/` – Create task
* `GET /api/tasks/{id}/` – Retrieve task
* `PUT /api/tasks/{id}/` – Update task
* `DELETE /api/tasks/{id}/` – Delete task

### 📍 Combined API Gateway (via User Service)

* `GET /api/user/{id}/tasks/` – Fetch user data along with all their tasks (calls task service internally)

---

## 🔬 Example Testing with Postman

1. **Create User**

```http
POST http://localhost:8000/api/users/
Content-Type: application/json

{
  "name": "John",
  "email": "john@example.com"
}
```

2. **Create Task**

```http
POST http://localhost:8001/api/tasks/
Content-Type: application/json

{
  "title": "Task",
  "description": "Do work",
  "user_id": 1
}
```

3. **Get User + Tasks Combined**

```http
GET http://localhost:8000/api/user/1/tasks/
```

---

## 📁 Project Structure

```
django-microservice-demo/
├── user_service/        # User service with DRF and gateway logic
├── task_service/        # Task service with separate DB and API
├── README.md            # Project documentation
```

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

## ✨ Author

Built with ❤️ by [Samandar Hamrayev](https://github.com/samandar-hamrayev)

```

---

Agar `requirements.txt` fayllar hali yozilmagan bo‘lsa, quyidagicha bo‘ladi:

### `user_service/requirements.txt`:
```

django>=4.2
djangorestframework
requests

```

### `task_service/requirements.txt`:
```
