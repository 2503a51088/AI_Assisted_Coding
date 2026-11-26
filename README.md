# AI-Assisted Smart Event Management & Collaboration Platform

## Project Overview

The AI-Assisted Smart Event Management & Collaboration Platform is a web-based application designed to simplify event creation, student registration, event management, and attendance tracking.

The platform provides an easy-to-use interface where students can create accounts, log in, view available events, register for events, and manage attendance.

## Features

- Student Registration
- Student Login
- Event Creation
- View All Events
- Student Event Registration
- Attendance Management
- Backend API Integration
- Database Management

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React.js |
| Backend | Python FastAPI |
| Database | SQLite |
| Programming Languages | Python, JavaScript |
| API Testing | Swagger UI |
| Code Editor | Visual Studio Code |

## Project Structure

```text
AI-Event-Management-Platform/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── index.html
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Backend Setup

Open the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Backend URL:

http://127.0.0.1:8000/

API Documentation:

http://127.0.0.1:8000/docs

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React application:

```bash
npm run dev
```

Frontend URL:

http://localhost:5173/

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home API |
| GET | `/events` | Get all events |
| POST | `/events` | Create an event |
| POST | `/register` | Student registration |
| POST | `/login` | Student login |
| POST | `/event-register` | Register for an event |
| POST | `/attendance` | Mark attendance |
| GET | `/attendance` | Get attendance records |

## Database

The application uses SQLite to store:

- Student details
- Event details
- Event registrations
- Attendance records

## Future Enhancements

- QR Code-Based Attendance
- Automated Email Notifications
- AI-Based Event Recommendations
- Event Scheduling and Reminders
- Advanced Analytics and Reports
- Online Deployment

## Conclusion

The AI-Assisted Smart Event Management & Collaboration Platform provides a centralized solution for managing events, student registrations, and attendance. It combines React, FastAPI, and SQLite to provide a simple and organized event management experience.

---

**Project:** AI-Assisted Smart Event Management & Collaboration Platform

**Product Number:** 14
