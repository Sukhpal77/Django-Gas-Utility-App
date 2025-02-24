# Gas Utility

This project is a gas utility management system designed to help users manage and monitor their gas usage efficiently.

## Features

- User registration and authentication
- Submit and manage service requests
- Track the status of service requests
- Admin interface for managing service requests
- Real-time gas usage monitoring
- Monthly usage reports
- Alerts for unusual usage patterns
- User-friendly interface

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Sukhpal77/Django-Gas-Utility-App.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Django-Gas-Utility-App
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
4. Install the Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser account:
    ```bash
    python manage.py createsuperuser
    ```

## Usage

1. Start the application:
    ```bash
    python manage.py runserver
    ```

Open your browser and go to `http://localhost:8000` or `http://127.0.0.1:8000/` to access the application.

### User Interface

- **Register**: Create a new account by filling out the registration form.
- **Login**: Log in with your credentials.
- **Submit Service Request**: After logging in, submit a new service request using the form on the home page.
- **Track Requests**: View the status of your service requests on the home page.

### Admin Interface

Access the admin interface at `http://127.0.0.1:8000/admin/` to manage service requests. Use the superuser credentials created earlier to log in.

## Project Structure

```
gas_utility/
├── gas_utility/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── registration/
│   │   │   │   ├── login.html
│   │   │   │   ├── register.html
│   │   │   ├── services/
│   │   │   │   ├── home.html
│   │   ├── urls.py
│   │   ├── views.py
│   ├── db.sqlite3
├── manage.py
```

## Contact

For any questions or feedback, please contact [sukhpalsingh0333@gmail.com](mailto:sukhpalsingh0333@gmail.com).
