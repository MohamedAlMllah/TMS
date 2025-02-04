Installation Guide
==================

Follow these steps to set up and run the API:

1. **Clone the Repository**

   .. code-block:: sh

      git clone https://github.com/mohamedalmllah/tms.git
      cd task-management-api

2. **Create and Activate a Virtual Environment**

   .. code-block:: sh

      python -m venv venv

      # Windows CMD
      venv\Scripts\activate

      # Windows PowerShell
      venv\Scripts\Activate.ps1

      # Mac/Linux/Git Bash
      source venv/bin/activate

3. **Install Dependencies**

   .. code-block:: sh

      pip install -r requirements.txt

4. **Run Migrations/seeders**

   .. code-block:: sh

      python manage.py makemigrations
      python manage.py migrate
      python manage.py seed_data

5. **Create a Superuser**

   .. code-block:: sh

      python manage.py createsuperuser

6. **Run the Server**

   .. code-block:: sh

      python manage.py runserver

**API will be available at:** `http://127.0.0.1:8000/api/`