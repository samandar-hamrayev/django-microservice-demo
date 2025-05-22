Django Microservice Demo
A microservices-based application using Django and Django REST Framework, featuring User Service and Task Service connected via user_id, with a combined API endpoint.
Overview

User Service: Manages user data (name, email) with CRUD APIs.
Task Service: Manages tasks (title, description, user_id) with CRUD APIs.
API Gateway: Combines user and task data at /api/user/{id}/tasks.

Technologies

Python 3.8+
Django 4.x
Django REST Framework
SQLite
Postman (for testing)

Setup

Clone Repository:
git clone https://github.com/samandar-hamrayev/django-microservice-demo.git
cd django-microservice-demo


Install User Service:
cd user_service
python -m venv venv
source venv/bin/activate
pip install django djangorestframework requests
python manage.py migrate


Install Task Service:
cd ../task_service
python -m venv venv
source venv/bin/activate
pip install django djangorestframework
python manage.py migrate


Run Services:

User Service: python manage.py runserver 8000
Task Service: python manage.py runserver 8001



API Endpoints

User Service (http://localhost:8000):
GET/POST /api/users/: List or create users.
GET/PUT/DELETE /api/users/{id}/: Get, update, or delete a user.


Task Service (http://localhost:8001):
GET/POST /api/tasks/: List (filter by ?user_id=) or create tasks.
GET/PUT/DELETE /api/tasks/{id}/: Get, update, or delete a task.


API Gateway:
GET /api/user/{id}/tasks/: Get user and their tasks.



Testing with Postman

Create User: POST http://localhost:8000/api/users/ with { "name": "John", "email": "john@example.com" }.
Create Task: POST http://localhost:8001/api/tasks/ with { "title": "Task", "description": "Do work", "user_id": 1 }.
Get User Tasks: GET http://localhost:8000/api/user/1/tasks/.

License
MIT License
