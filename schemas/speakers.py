from pydantic import BaseModel, Field
from typing import Optional

class SpeakerBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the speaker")
    topic: str = Field(..., min_length=1, max_length=200, description="Topic they will be description")

class SpeakerCreate(SpeakerBase):
    pass

class SpeakerUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    topic: Optional[str] = Field(None, min_length=1, max_length=200)

class Speaker(SpeakerBase):
    id: int = Field(..., description="Unique identifier for the speaker")

class Config:
    from_attributes = True
