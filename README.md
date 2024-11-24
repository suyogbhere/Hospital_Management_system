# Project Name  (Hospital Management System)

- https://github.com/suyogbhere/Hospital_Management_system


- Python Version: Python 3.12.0
- Bootstrap Version: 5.0
- Database version: Postgresql 17

## Features

- Feature 1: staff, patient, doctor can Signup, Login, logout
- Feature 2: 
- Feature 3: 
- Feature 4: Django authentication 
- Feature 5: Only authenticated user can view inside project feature.

## Demo


## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/suyogbhere/Hospital_Management_system
    cd https://github.com/suyogbhere/hospital_management_system
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. cd hospital_management_system

5. Apply migrations (if applicable):
    ```bash
    python manage.py migrations
    python manage.py migrate
    ```
6. If you want your own superuser account run below commmand
    python manage.py createsuperuser

7. Start the development server:
    ```bash
    python manage.py runserver


## Usage

- Access the portal at http://127.0.0.1:8000
- Log in using default admin credentials (set in the admin panel).


## project Urls

1. http://127.0.0.1:8000/register/
2. http://127.0.0.1:8000/login/
