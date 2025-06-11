from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.event import Event, EventCreate, EventUpdate
from services import event_service

router = APIRouter()

@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event(event_data: EventCreate):
    """Create a new event"""
    event = event_service.create_event(event_data)
    return event

@router.get("/", response_model=List[Event])
async def get_all_events():
    """Get all events"""
    return event_service.get_all_events()

@router.get("/{event_id}", response_model=Event)
async def get_event(event_id: int):
    """Get a specific event by ID"""
    event = event_service.get_event(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return event

@router.put("/{event_id}", response_model=Event)
async def update_event(event_id: int, event_data: EventUpdate):
    """Update an event"""
    event = event_service.update_event(event_id, event_data)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return event

@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(event_id: int):
    """Delete an event"""
    if not event_service.delete_event(event_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )

@router.patch("/{event_id}/close", response_model=Event)
async def close_event_registration(event_id: int):
    """Close event registration (set is_open to False)"""
    event = event_service.close_event_registration(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return event