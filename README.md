#  Secure Flask Login System

This project is a secure Flask-based web application developed during an online internship program at **Cryptonic Area**.
The main objective is to practice **secure authentication, session management, and access control** in a web application.

---

##  Project Overview

The application provides:

* Secure user authentication (login/logout)
* Session-based authorization
* Protected routes for authenticated users only
* Password policy enforcement
* Basic security best practices in Flask

This project focuses on **understanding security concepts** rather than building a production-ready system.

---

##  Technologies Used

* Python
* Flask
* HTML & CSS
* Werkzeug (password hashing)
* Regular Expressions (input validation)

---

##  Authentication & Authorization Flow

1. User logs in with username and password
2. Credentials are validated using hashed passwords
3. Password policy is enforced (8+ characters, uppercase, lowercase, number, special character)
4. A secure session is created after successful login
5. Dashboard is accessible only to authenticated users
6. Logout clears the session and prevents back-button access

---

##  Security Features

* Password hashing using Werkzeug
* Session expiration after 30 minutes
* HttpOnly and SameSite cookie settings
* Access control for protected routes
* Cache-control headers to prevent unauthorized access after logout
* Input validation for usernames and passwords

---

##  Demo Users

For demonstration purposes only:

* **admin / Admin@123**
* **lale / Lale@123**
* **test / Test@123**

---

##  Installation & Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:

   ```bash
   python app.py
   ```
5. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

##  Internship Information

This project was built during the **Cryptonic Area Virtual Internship Program**.

### What I learned during this project:

* Flask authentication and routing
* Secure session handling
* Password hashing and policy enforcement
* Preventing authentication bypass
* Browser cache security handling
* Structuring a secure Flask application

---

##  Future Improvements

* Database integration (SQLite / PostgreSQL)
* User registration system
* Role-based access control
* HTTPS deployment

---

##  Author

**Lala Alili**
Information Security Student
