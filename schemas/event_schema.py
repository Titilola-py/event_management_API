from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class EventBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Name of the event")
    location: str = Field(..., min_length=1, max_length=200, description="Location of the event")
    date: date = Field(..., description="Date of the event")

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    location: Optional[str] = Field(None, min_length=1, max_length=200)
    date: Optional[date] = None
    is_open: Optional[bool] = None

class Event(EventBase):
    id: int = Field(..., description="Unique identifier for the event")
    is_open: bool = Field(default=True, description="Whether the event is accepting new attendees")

class Config:
    from_attributes = True
