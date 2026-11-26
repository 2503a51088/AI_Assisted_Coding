from pydantic import BaseModel, Field


class UserRegister(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str


class EventCreate(BaseModel):
    title: str
    description: str
    date: str
    venue: str


class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    date: str
    venue: str

    class Config:
        from_attributes = True


# Attendance Request
class AttendanceCreate(BaseModel):
    registration_id: int
    status: str = "Present"


# Attendance Response
class AttendanceResponse(BaseModel):
    id: int
    registration_id: int
    status: str

    class Config:
        from_attributes = True