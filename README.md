# 🧑‍💼 Job Portal

A full-stack Job Portal application built with **React** (frontend) and **Django** (backend).  
This project allows job seekers to browse and apply for jobs, while employers can post and manage job listings.

---

## 🚀 Features

### For Job Seekers
- User registration & authentication
- Profile creation and resume upload
- Browse and search job listings
- Apply for jobs directly from the portal
- Track application status

### For Employers
- Employer registration & authentication
- Post new job listings
- Manage and edit job postings
- View applicants for each job

### General
- Secure authentication with JWT
- RESTful API powered by Django REST Framework
- Responsive UI built with React
- PostgreSQL/MySQL database support

---

## 🛠️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | React, React Router, Axios |
| Backend      | Django, Django REST Framework |
| Database     | PostgreSQL (or MySQL/SQLite) |
| Authentication | JWT (JSON Web Tokens) |
| Deployment   | Docker / GitHub Actions (optional) |

---

## 📂 Project Structure


job-portal/ │ ├── backend/              # Django project │   ├── job_portal/       # Main Django app │   ├── api/              # REST API endpoints │   └── requirements.txt │ ├── frontend/             # React project │   ├── src/ │   │   ├── components/   # Reusable UI components │   │   ├── pages/        # Page-level components │   │   └── services/     # API calls │   └── package.json │ └── README.md



---

## ⚙️ Installation & Setup

### Backend (Django)
```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

cd frontend
npm install
npm start
