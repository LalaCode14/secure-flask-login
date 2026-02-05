🔐 Secure Flask Login System
Built during an online internship program
Organization: Cryptonic Area
This project is a secure Flask-based web application developed as part of an online internship program.
The main goal of this project is to understand and implement secure authentication, session management, and access control mechanisms in a web application.
________________________________________
📌 Project Overview
The application provides:
•	Secure user authentication (login/logout)
•	Session-based authorization
•	Protected routes accessible only to authenticated users
•	Password policy enforcement
•	Basic security best practices implemented in Flask
This project focuses on learning security concepts, not just building a working app.
________________________________________
⚙️ Technologies Used
•	Python
•	Flask
•	HTML & CSS
•	Werkzeug (Password Hashing)
•	Regular Expressions (Input Validation)
________________________________________
🔑 Authentication & Authorization Flow
1.	User logs in using a username and password
2.	Credentials are validated and passwords are checked using hashed values
3.	Password must meet policy: 8+ chars, uppercase, lowercase, number, special symbol
4.	A secure session is created after successful login
5.	The dashboard page is accessible only to authenticated users
6.	User can log out, which clears the session
________________________________________
🛡️ Security Features Implemented
•	Password Hashing
Passwords are stored using Werkzeug's secure hashing functions.
•	Session Handling
Sessions expire automatically after 30 minutes. HttpOnly and SameSite cookies are used.
•	Access Control
Protected routes cannot be accessed without authentication.
•	Cache Control Protection
Browser back-button access after logout is prevented using no-cache headers.
•	Input Validation
Username format and password policy are enforced.
________________________________________
👥 Demo Users
For demonstration purposes, user accounts are predefined:
Username	Password
admin	Admin@123
lale	Lale@123
test	Test@123
________________________________________
📸 Screenshots
Screenshots included:
•	Login Page
•	Dashboard Page
•	Unauthorized access redirection
________________________________________
📚 What I Learned
•	Flask authentication and routing
•	Secure session management
•	Password hashing and policy enforcement
•	Preventing authentication bypass
•	Handling browser cache security issues
•	Structuring a secure Flask web application
________________________________________
🏢 Internship Information
•	Built during an online internship program
•	Organization: Cryptonic Area
•	Focus: Security fundamentals and secure web development
________________________________________
🚀 Future Improvements
•	Database integration (SQLite/PostgreSQL)
•	User registration system
•	Role-based access control
•	HTTPS deployment
________________________________________
📎 Author
Lala
Information Security Student


