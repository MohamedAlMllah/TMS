Authentication Guide
====================

This API uses Djoser for authentication.

1. **Register a New User**
   
   .. code-block:: http

      POST /api/auth/users/
      Content-Type: application/json
      {
          "username": "testuser",
          "password": "securepassword"
      }

2. **Login & Get Token**
   
   .. code-block:: http

      POST /api/auth/token/login/
      Content-Type: application/json
      {
          "username": "testuser",
          "password": "securepassword"
      }

   **Response:**
   
   .. code-block:: json

      {
          "auth_token": "your-auth-token"
      }

3. **Use the Token in Requests**
   
   .. code-block:: http

      Authorization: Token your-auth-token
