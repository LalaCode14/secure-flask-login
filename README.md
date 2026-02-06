# Secure Flask Login System

This project is a secure Flask-based web application developed during an online internship program at **Cryptonic Area**.  
The main objective is to practice secure authentication, session management, and access control in a web application.

## Project Overview
The application provides:
- Secure user authentication (login/logout)
- Session-based authorization
- Protected routes for authenticated users only
- Password policy enforcement
- Basic security best practices in Flask

This project focuses on understanding security concepts rather than building a production-ready system.

## Technologies Used
- Python
- Flask
- HTML & CSS
- Werkzeug (password hashing)
- Regular Expressions (input validation)

## Authentication & Authorization Flow
- User logs in with username and password
- Credentials are validated using hashed passwords
- Password policy enforced (8+ characters, uppercase, lowercase, number, special character)
- A secure session is created after successful login
- Dashboard is accessible only to authenticated users
- Logout clears the session and prevents back-button access

## Security Features
- Password hashing using Werkzeug
- Session expiration after 30 minutes
- HttpOnly and SameSite cookie settings
- Access control for protected routes
- Cache-control headers to prevent unauthorized access after logout
- Input validation for usernames and passwords

## Demo Users
For demonstration purposes only:
- **admin / Admin@123**
- **lale / Lale@123**
- **test / Test@123**

## What I Learned
- Flask authentication and routing
- Secure session handling
- Password hashing and policy enforcement
- Preventing authentication bypass
- Browser cache security handling
- Structuring a secure Flask application

## Internship Information
- Online internship program
- Organization: Cryptonic Area
- Focus: Security fundamentals and secure web development

## Future Improvements
- Database integration (SQLite/PostgreSQL)
- User registration system
- Role-based access control
- HTTPS deployment

## Author
**Lala Alili**  
Information Security Student
