from typing import Dict, List, Optional
from schemas.event import Event, EventCreate, EventUpdate

events_db: Dict[int, Event] = {}
event_id_counter = 1

def create_event(event_data: EventCreate) -> Event:
    global event_id_counter

    event = Event(
        id=event_id_counter,
        title=event_data.title,
        location=event_data.location,
        event_date=event_data.event_date, 
        is_open=True
    )
    events_db[event_id_counter] = event
    event_id_counter += 1
    return event

def get_event(event_id: int) -> Optional[Event]:
    return events_db.get(event_id)

def get_all_events() -> list[Event]:
    return list(events_db.values())

def update_event(event_id: int, event_data: EventUpdate) -> Optional[Event]:
    if event_id not in events_db:
        return None
    
    event= events_db[event_id]
    update_data = event_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(event, field, value)

    return event

def delete_event(event_id: int) -> bool:
    if event_id in events_db:
        del events_db[event_id]
        return True
    return False

def close_event_registration(event_id: int) -> Optional[Event]:
    if event_id not in events_db:
        return None

    events_db[event_id].is_open = False
    return events_db[event_id]