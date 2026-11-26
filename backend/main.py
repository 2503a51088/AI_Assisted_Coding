from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import engine, Base, get_db
import models
import schemas
from auth import hash_password, verify_password

# Import AI recommendation function
from ai_recommendation import recommend_events


app = FastAPI(
    title="AI-Assisted Smart Event Management Platform",
    description="Smart Event Management System with AI Recommendations",
    version="1.0"
)

# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)


class EventRegistrationRequest(BaseModel):
    user_id: int
    event_id: int


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Event Management Platform",
        "status": "Running Successfully"
    }


# Get all events
@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(models.Event).all()


# Create event
@app.post("/events")
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    new_event = models.Event(
        title=event.title,
        description=event.description,
        date=event.date,
        venue=event.venue
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return {
        "message": "Event created successfully",
        "event_id": new_event.id
    }


# Student registration
@app.post("/register")
def register_user(user: schemas.UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role="student"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Registration successful",
        "user_id": new_user.id
    }


# Student login
@app.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "message": "Login successful",
        "user_id": existing_user.id,
        "name": existing_user.name,
        "role": existing_user.role
    }


# Register student for an event
@app.post("/event-register")
def register_event(
    registration: EventRegistrationRequest,
    db: Session = Depends(get_db)
):
    existing_user = db.query(models.User).filter(
        models.User.id == registration.user_id
    ).first()

    if not existing_user:
        raise HTTPException(status_code=404, detail="Student not found")

    existing_event = db.query(models.Event).filter(
        models.Event.id == registration.event_id
    ).first()

    if not existing_event:
        raise HTTPException(status_code=404, detail="Event not found")

    existing_registration = db.query(models.Registration).filter(
        models.Registration.user_id == registration.user_id,
        models.Registration.event_id == registration.event_id
    ).first()

    if existing_registration:
        raise HTTPException(
            status_code=400,
            detail="Student already registered for this event"
        )

    new_registration = models.Registration(
        user_id=registration.user_id,
        event_id=registration.event_id
    )

    db.add(new_registration)
    db.commit()
    db.refresh(new_registration)

    return {
        "message": "Event registration successful",
        "registration_id": new_registration.id,
        "user_id": new_registration.user_id,
        "event_id": new_registration.event_id
    }


# Mark attendance
@app.post("/attendance")
def mark_attendance(
    attendance: schemas.AttendanceCreate,
    db: Session = Depends(get_db)
):
    if attendance.status not in ["Present", "Absent"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be Present or Absent"
        )

    existing_registration = db.query(models.Registration).filter(
        models.Registration.id == attendance.registration_id
    ).first()

    if not existing_registration:
        raise HTTPException(status_code=404, detail="Registration not found")

    existing_attendance = db.query(models.Attendance).filter(
        models.Attendance.registration_id == attendance.registration_id
    ).first()

    if existing_attendance:
        raise HTTPException(status_code=400, detail="Attendance already marked")

    new_attendance = models.Attendance(
        registration_id=attendance.registration_id,
        status=attendance.status
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return {
        "message": "Attendance marked successfully",
        "attendance_id": new_attendance.id,
        "registration_id": new_attendance.registration_id,
        "status": new_attendance.status
    }


# Get attendance records
@app.get("/attendance")
def get_attendance(db: Session = Depends(get_db)):
    return db.query(models.Attendance).all()


# AI EVENT RECOMMENDATIONS
@app.get("/recommend-events")
def get_recommended_events(
    interests: str,
    db: Session = Depends(get_db)
):
    if not interests.strip():
        raise HTTPException(
            status_code=400,
            detail="Please enter your interests"
        )

    events = db.query(models.Event).all()

    event_data = [
        {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "date": event.date,
            "venue": event.venue
        }
        for event in events
    ]

    recommendations = recommend_events(interests, event_data)

    return {
        "message": "AI recommendations generated successfully",
        "interests": interests,
        "recommendations": recommendations
    }