# Leave Management System

This is a web-based application for managing leave requests. It allows users to apply for leave, track the status of their leave, and ensures that there are no overlapping leave requests for the same dates. The application is built using Django and provides both staff and user roles.

## Features

- **Staff Role**: Staff members can apply for leave and view leave statuses.
- **hod Role**: hod can be able to approve and reject the leaves.
- **Leave Request Form**: Users can fill in the reason for leave and the start and end dates.
- **Date Validation**: The application checks if a user has already applied for leave on the same dates.

## Requirements

- Python 3.8 or higher
- Django 3.x
- SQLite (default) or any other database backend

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Jinal-81/leave_management.git
   cd leave_management


1. **Create a virtual environment and activate it:**

```python -m venv venv```
# On Windows
```venv\Scripts\activate```
# On macOS/Linux
```source venv/bin/activate```

- Install the required dependencies:

- pip install -r requirements.txt

2. **Set up the database:**

```python manage.py migrate```

- Create a superuser to access the admin panel:

```python manage.py createsuperuser```

- Run the development server:

```python manage.py runserver```

- Visit the application at http://127.0.0.1:8000/
