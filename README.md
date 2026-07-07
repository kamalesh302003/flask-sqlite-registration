# 🔐 Flask Authentication System

A secure and beginner-friendly **User Authentication System** built using **Python Flask** and **SQLite3**. This project allows users to register and log in through a simple web interface while storing user information in an SQLite database.

## 📌 Features

- ✅ User Registration
- ✅ User Login Authentication
- ✅ SQLite3 Database Integration
- ✅ Duplicate Email Prevention
- ✅ Responsive HTML Templates
- ✅ Success Page After Registration/Login
- ✅ Flask Routing
- ✅ Secure SQL Queries Using Parameterized Statements
- ✅ Easy to Understand Code Structure
- ✅ Beginner-Friendly Project

## 🛠️ Technologies Used

- Python 3
- Flask
- SQLite3
- HTML5
- CSS3
- Jinja2 Templates

## 📂 Project Structure
Flask-Authentication-System/
│
├── app.py
├── pythonflask.db
│
├── templates/
│   ├── register.html
│   ├── login.html
│   └── success.html
│
├── static/
│   ├── css/
│   └── images/
│
├── README.md
└── requirements.txt

Install Dependencies

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```
 Run the Application

```bash
python app.py
```
Open your browser and visit:

```
http://127.0.0.1:5000
```

## 🗄️ Database

The project uses **SQLite3** as the database.

Database file:

```
pythonflask.db
```

Table:

```
reg
```

Columns:

| Column | Type |
|---------|------|
| UNAME | TEXT |
| EMAIL | TEXT (UNIQUE) |
| UPASS | TEXT |

---

## 🔄 Application Workflow

```
Home Page
      │
      ▼
Registration Page
      │
      ▼
User Registration
      │
      ▼
Data Stored in SQLite Database
      │
      ▼
Login Page
      │
      ▼
User Authentication
      │
      ├──────────────┐
      ▼              ▼
Login Success   Invalid Credentials
```

---

## 💻 SQL Operations

### Insert User

```sql
INSERT INTO reg (UNAME, EMAIL, UPASS)
VALUES (?, ?, ?)
```

### Login Verification

```sql
SELECT UNAME
FROM reg
WHERE EMAIL=? AND UPASS=?
```

---

## 📸 Screenshots

Add screenshots of the following pages:

- 📝 Registration Page
- 🔑 Login Page
- 🎉 Success Page
- 🗄️ SQLite Database

---

## 🚀 Future Improvements
- Password Hashing (Werkzeug)
- User Session Management
- Logout Functionality
- Forgot Password
- Email Verification
- Password Strength Validation
- Flash Messages
- Dashboard
- User Profile Page
- Bootstrap 5 UI
- Dark Mode
- Remember Me Feature
- Role-Based Authentication (Admin/User)
- Account Lock After Multiple Failed Attempts

## 🎯 Learning Outcomes
Through this project, you will understand:
- Flask Routing
- HTML Forms
- Jinja2 Templates
- SQLite3 Database Operations
- CRUD Basics
- User Authentication
- SQL Parameterized Queries
- Python Functions
- Web Application Development

If you found this project useful, consider giving it a ⭐ on GitHub. Your support helps motivate future improvements and new open-source projects.
