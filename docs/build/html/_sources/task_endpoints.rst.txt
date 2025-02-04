Task Management API Endpoints
=============================

1. **Get All Tasks Assigned To User**
  
   .. code-block:: http

      GET /api/tasks/
      Authorization: Token user-token

2. **Get All Tasks (Manager Only)**
  
   .. code-block:: http

      GET /api/tasks/
      Authorization: Token manager-token

3. **Create a Task (Manager Only)**
  
   .. code-block:: http

      POST /api/tasks/
      Authorization: Token manager-token
      Content-Type: application/json
      {
          "title": "New Task",
          "description": "Task Description",
          "assignee": 2,
          "due_date": "2024-02-10"
      }

4. **Update Task Status (User)**
  
   .. code-block:: http

      PATCH /api/tasks/1/
      Authorization: Token user-token
      Content-Type: application/json
      {
          "status": "completed"
      }

5. **Update Task Full Details (Manager Only)**
  
   .. code-block:: http

      PATCH /api/tasks/1/
      Authorization: Token manager-token
      Content-Type: application/json
      {
          "title": "New Task Title",
          "description": "Task Description",
          "assignee": 3,
          "due_date": "2024-02-15"
      }

6. **Delete Task (Manager Only)**
  
   .. code-block:: http

      DELETE /api/tasks/1/
      Authorization: Token manager-token
