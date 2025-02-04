# 🚀 Task Management System API

A RESTful Task Management API built with **Django REST Framework (DRF)** and **Djoser authentication**.

## 📌 Features
✅ User authentication (via **Djoser**)  
✅ Role-based access (**Managers & Users**)  
✅ Task creation, assignment & filtering  
✅ Task dependencies (A task cannot be completed until dependencies are done)  
✅ Token-based authentication  

---

## 📌 1️⃣ Installation Guide

### **Clone the Repository**
```sh
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api


Create & Activate Virtual Environment
sh
Copy
Edit
python -m venv venv

# Windows CMD
venv\Scripts\activate

# Windows PowerShell
venv\Scripts\Activate.ps1

# macOS/Linux/Git Bash
source venv/bin/activate
Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
Apply Migrations
sh
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create a Superuser
sh
Copy
Edit
python manage.py createsuperuser
Run the Server
sh
Copy
Edit
python manage.py runserver
✅ API will be available at: http://127.0.0.1:8000/api/

📌 2️⃣ Authentication Endpoints (Djoser)
🔹 Register a New User
http
Copy
Edit
POST /api/auth/users/
Content-Type: application/json
{
    "username": "testuser",
    "password": "securepassword"
}
🔹 Login & Get Token
h
Copy
Edit
POST /api/auth/token/login/
Content-Type: application/json
{
    "username": "testuser",
    "password": "securepassword"
}
✅ Response:

json
Copy
Edit
{
    "auth_token": "your-auth-token"
}
💡 Use the token in requests:

makefile
Copy
Edit
Authorization: Token your-auth-token
📌 3️⃣ Task Management Endpoints
🔹 Get All Tasks
http
Copy
Edit
GET /api/tasks/
Authorization: Token user-token
🔹 Create a Task (Manager Only)
http
Copy
Edit
POST /api/tasks/
Authorization: Token manager-token
Content-Type: application/json
{
    "title": "New Task",
    "description": "Task Description",
    "assignee": 2,
    "due_date": "2024-02-10"
}
🔹 Update Task Status (User)
http
Copy
Edit
PATCH /api/tasks/1/
Authorization: Token user-token
Content-Type: application/json
{
    "status": "completed"
}
🔹 Delete Task (Manager Only)
http
Copy
Edit
DELETE /api/tasks/1/
Authorization: Token manager-token
📌 4️⃣ Run Tests
sh
Copy
Edit
python manage.py test
📌 5️⃣ Contributors
Your Name - Maintainer
Contributions are welcome! 🎉
📌 6️⃣ License
This project is MIT Licensed. Feel free to modify and use it! 📝

yaml
Copy
Edit

---

## **📌 Step 3: Commit & Push the README**
After creating the `README.md`, commit and push it to GitHub:

```sh
git add README.md
git commit -m "Added project README"
git push origin main  # Change 'main' if using a different branch
