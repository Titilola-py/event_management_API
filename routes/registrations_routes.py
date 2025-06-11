from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.registration import Registration, RegistrationCreate, RegistrationUpdate
from services import registration_service

router = APIRouter()

@router.post("/", response_model=Registration, status_code=status.HTTP_201_CREATED)
async def register_user_for_event(registration_data: RegistrationCreate):
    """Register a user for an event"""
    try:
        registration = registration_service.create_registration(registration_data)
        return registration
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/", response_model=List[Registration])
async def get_all_registrations():
    """Get all registrations"""
    return registration_service.get_all_registrations()

@router.get("/{registration_id}", response_model=Registration)
async def get_registration(registration_id: int):
    """Get a specific registration by ID"""
    registration = registration_service.get_registration(registration_id)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return registration

@router.get("/user/{user_id}", response_model=List[Registration])
async def get_registrations_by_user(user_id: int):
    """Get all registrations for a specific user"""
    return registration_service.get_registrations_by_user(user_id)

@router.get("/event/{event_id}", response_model=List[Registration])
async def get_registrations_by_event(event_id: int):
    """Get all registrations for a specific event"""
    return registration_service.get_registrations_by_event(event_id)

@router.patch("/{registration_id}/attend", response_model=Registration)
async def mark_attendance(registration_id: int):
    """Mark attendance for a registration (set attended to True)"""
    registration = registration_service.mark_attendance(registration_id)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return registration

@router.put("/{registration_id}", response_model=Registration)
async def update_registration(registration_id: int, registration_data: RegistrationUpdate):
    """Update a registration"""
    registration = registration_service.update_registration(registration_id, registration_data)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return registration

@router.delete("/{registration_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_registration(registration_id: int):
    """Delete a registration"""
    if not registration_service.delete_registration(registration_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )

# Optional endpoint: Filter users who attended at least one event
@router.get("/analytics/attendees", response_model=List[int])
async def get_users_who_attended():
    """Get user IDs of users who attended at least one event"""
    return registration_service.get_users_who_attended_events()