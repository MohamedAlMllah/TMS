# 🚀 Task Management System API

A RESTful Task Management API built with **Django REST Framework (DRF)** and **Djoser authentication**.

## 📌 Features
✅ User authentication (via **Djoser**)  
✅ Role-based access (**Managers & Users**)  
✅ Task creation, assignment & filtering  
✅ Task dependencies (A task cannot be completed until dependencies are done)  

![image](https://github.com/user-attachments/assets/76a04a19-d120-47d7-8b0e-8ad97dd1f1bc)

---

## 📌 1️⃣ Installation Guide

Clone the Repository
```
git clone https://github.com/mohamedalmllah/tms.git
cd tms
```
🔹 After cloning the repository, you can check Task Management API Documentation at: TMS/docs/build/html/index.html 🔹
![image](https://github.com/user-attachments/assets/6a6140cf-d17f-4cdb-b49a-68245d1df106)


Create & Activate Virtual Environment
```
python -m venv venv

# Windows CMD
venv\Scripts\activate

# Windows PowerShell
venv\Scripts\Activate.ps1

# Mac/Linux
source venv/bin/activate

# Git Bash
source venv/Scripts/activate
```
Install Dependencies
```
pip install djoser djangorestframework
```
Apply Migrations/Seeders
```
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
```
Create a Superuser
```
python manage.py createsuperuser
```
💡 Superuser can access Django administration at: http://127.0.0.1:8000/admin/

![image](https://github.com/user-attachments/assets/4e8cd13f-7e22-4dfe-900c-06169f8d03c3)

Run the Server
```
python manage.py runserver
```
✅ API will be available at: http://127.0.0.1:8000/api/

## 📌 2️⃣ Authentication Endpoints (Djoser)
🔹 Register a New User
```
POST /api/auth/users/
Content-Type: application/json
{
    "username": "testuser",
    "password": "securepassword"
}
```
🔹 Login & Get Token
```
POST /api/auth/token/login/
Content-Type: application/json
{
    "username": "testuser",
    "password": "securepassword"
}
```
✅ Response:
```
{
    "auth_token": "your-auth-token"
}
```
💡 Use the token in requests
## 📌 3️⃣ Task Management Endpoints
🔹 Get All Tasks
```
GET /api/tasks/
Authorization: Token user-token
```
🔹 Create a Task (Manager Only)
```
POST /api/tasks/
Authorization: Token manager-token
Content-Type: application/json
{
    "title": "New Task",
    "description": "Task Description",
    "assignee": 2,
    "due_date": "2024-02-10"
}
```
🔹 Update Task Status (User)
```
PATCH /api/tasks/1/
Authorization: Token user-token
Content-Type: application/json
{
    "status": "completed"
}
```
🔹 Delete Task (Manager Only)
```
DELETE /api/tasks/1/
Authorization: Token manager-token
```
## 📌 4️⃣ Login Credentials (Seeder)
When you run the seeder, the following test data is created:

### **Users**
| Username  | Role       | Password       |
|-----------|------------|----------------|
| admin     | Superuser  | abc@2025       |
| manager1  | Manager    | abc@2025       |
| user1     | User       | abc@2025       |
