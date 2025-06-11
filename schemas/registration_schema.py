from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RegistrationBase(BaseModel):
    user_id: int = Field(..., description="ID of the registering user")
    event_id: int = Field(..., description="ID of the event")

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationUpdate(BaseModel):
    attended: Optional[bool] = None

class Registration(RegistrationBase):
    id: int = Field(..., description="Unique identifier for the registration")
    registration_date: datetime = Field(default_factory=datetime.now, description="When the user registered")
    attended: bool = Field(default=False, description="Whether the user attended")

class Config:
    from_attributes = True 