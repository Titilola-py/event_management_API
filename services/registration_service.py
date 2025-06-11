from typing import Dict, List, Optional
from datetime import datetime
from schemas.registration import Registration, RegistrationCreate, RegistrationUpdate
from services.event_service import get_event
from services.user_service import get_user

registrations_db: Dict[int, Registration] = {}
registration_id_counter = 1

def create_registration(registration_data: RegistrationCreate) -> Registration:
    global registration_id_counter

    # Check if user exists
    user = get_user(registration_data.user_id)
    if not user:
        raise ValueError("User not found")
    
    # Check if user is active (assuming user has an 'active' field)
    if hasattr(user, 'active') and not user.active:
        raise ValueError("Only active users can register for event")
    
    # Check if event exists
    event = get_event(registration_data.event_id)
    if not event:
        raise ValueError("Event not found")
    
    # Check if user is already registered for this event
    for registration in registrations_db.values():
        if (registration.user_id == registration_data.user_id and
            registration.event_id == registration_data.event_id):
            raise ValueError("User is already registered for this event")
        
    registration = Registration(
        id=registration_id_counter,
        user_id=registration_data.user_id,
        event_id=registration_data.event_id,
        registration_date=datetime.now(),
        attended=False
    )
    registrations_db[registration_id_counter] = registration
    registration_id_counter += 1 
    return registration

def get_registration(registration_id: int) -> Optional[Registration]:
    return registrations_db.get(registration_id)

def get_all_registrations() -> List[Registration]:
    return list(registrations_db.values())

def get_registrations_by_user(user_id: int) -> List[Registration]:
    return [reg for reg in registrations_db.values() if reg.user_id == user_id]

def get_registrations_by_event(event_id: int) -> List[Registration]:
    return [reg for reg in registrations_db.values() if reg.event_id == event_id]

def mark_attendance(registration_id: int) -> Optional[Registration]:
    if registration_id not in registrations_db:
        return None
    
    registrations_db[registration_id].attended = True
    return registrations_db[registration_id]

def update_registration(registration_id: int, registration_data: RegistrationUpdate) -> Optional[Registration]:
    if registration_id not in registrations_db: 
        return None
    
    registration = registrations_db[registration_id]
    update_data = registration_data.model_dump(exclude_unset=True) 

    for field, value in update_data.items():
        setattr(registration, field, value)

    return registration

def delete_registration(registration_id: int) -> bool:
    if registration_id in registrations_db:
        del registrations_db[registration_id]
        return True
    return False

def get_users_who_attended_events() -> List[int]:
    """Optional: Get user IDs who attended at least one event"""
    attended_users = set()
    for registration in registrations_db.values():
        if registration.attended:
            attended_users.add(registration.user_id)
    return list(attended_users)