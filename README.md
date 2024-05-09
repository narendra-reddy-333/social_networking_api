# Social Networking API (Django)

**Project Description:**

This project implements a RESTful API for a social networking application using Django and Django REST Framework (DRF). The API provides functionalities for user registration, login, user search, sending/accepting/rejecting friend requests, and listing friends/pending requests.

**Technology Stack:**

* **Backend:** Python, Django, Django REST Framework (DRF), djangorestframework-simplejwt
* **Database:** SQLite (can be easily replaced with other databases like PostgreSQL)
* **Containerization:** Docker (optional, for development and deployment)

**Features:**

* **User Management:**
    * Registration with email and password.
    * Login with email and password (case-insensitive).
    * Search for users by email or name.

* **Friend Management:**
    * Send, accept, and reject friend requests.
    * List a user's friends (accepted friend requests).
    * View pending friend requests.

* **Authentication:**
    * Uses JWT (JSON Web Tokens) for secure authentication.
    * Provides endpoints to obtain and refresh tokens.

* **Rate Limiting:**
    * Limits the rate of friend requests to prevent spam.

### **Installation:**

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git

2. **Navigate to the project directory:**
   ```bash
    cd <your-repo-name>

3. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
4. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
6. **Run migrations:**
   ```bash
   python manage.py migrate
   
7. **Create a superuser (for Django admin):**
   ```bash
   python manage.py createsuperuser
   
8. **Run the development server:**
   ```bash
   python manage.py runserver
   
9. **Run migrations:**
   ```bash
   python manage.py migrate
   
10. **Run migrations:**
    ```bash
    python manage.py migrate
    

### API Endpoints:

1. `/api/users/register/` - Register new users (POST)
2. `/api/users/login/` - Login and obtain JWT tokens (POST)
3. `/api/users/search/` - Search for users by email or name (GET)
4. `/api/friends/requests/` - Send a friend request (POST)
5. `/api/friends/requests/` - Get Pending friend requests (GET)
6. `/api/friends/requests/{request_id}/` - Accept/reject a friend request (PUT/PATCH)
7. `/api/friends/` - List a user's friends (GET)
8. `/api/token/refresh`/ - Refresh JWT tokens (POST)


#### Authentication:

    Include the JWT access token in the Authorization header of requests (e.g., `Authorization: Bearer <YOUR_ACCESS_TOKEN>`).

#### Postman Collection:

   Create a Postman collection with requests for each API endpoint, including examples and documentation to facilitate easy testing and evaluation.


