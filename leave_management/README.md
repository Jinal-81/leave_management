# Leave Management System

This is a web-based application for managing leave requests. It allows users to apply for leave, track the status of their leave, and ensures that there are no overlapping leave requests for the same dates. The application is built using Django and provides both staff and user roles.

## Features

- **Staff Role**: Staff members can apply for leave and view leave statuses.
- **User Role**: Regular users can apply for leave, but their requests will be checked for overlapping dates.
- **Leave Request Form**: Users can fill in the reason for leave and the start and end dates.
- **Date Validation**: The application checks if a user has already applied for leave on the same dates.

## Requirements

- Python 3.8 or higher
- Django 3.x
- SQLite (default) or any other database backend

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/leave-management-system.git
   cd leave-management-system
