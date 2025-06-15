# Event Management API

A FastAPI-based system for managing events, users, speakers, and registrations. This API allows users to register for events, track attendance, and manage event information with proper validation and relationships.

## Features

- **User Management**: Create, read, update, delete users with email validation
- **Event Management**: Full CRUD operations for events with date and location tracking
- **Speaker Management**: Manage speakers and their presentation topics
- **Registration System**: Register users for events with attendance tracking
- **Validation**: Comprehensive validation rules and business logic
- **Interactive Documentation**: Auto-generated API documentation with Swagger UI

## Requirements

- Python 3.12.4
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Titilola-py/event_management_API
   cd event_management_api
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the server**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**
   - API Base URL: http://localhost:8000
   - Interactive Documentation: http://localhost:8000/docs
   - Alternative Documentation: http://localhost:8000/redoc

## Project Structure

```
event_management_api/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── schemas/               # Pydantic models for data validation
│   ├── __init__.py
│   ├── user.py           # User schemas
│   ├── event.py          # Event schemas
│   ├── speaker.py        # Speaker schemas
│   └── registration.py   # Registration schemas
├── routes/                # API route handlers
│   ├── __init__.py
│   ├── users.py          # User endpoints
│   ├── events.py         # Event endpoints
│   ├── speakers.py       # Speaker endpoints
│   └── registrations.py  # Registration endpoints
└── services/              # Business logic layer
    ├── __init__.py
    ├── user_service.py    # User business logic
    ├── event_service.py   # Event business logic
    ├── speaker_service.py # Speaker business logic
    └── registration_service.py # Registration business logic
```

## API Endpoints

### Users (`/users`)

- `POST /users/` - Create a new user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get a specific user
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user
- `PATCH /users/{user_id}/deactivate` - Deactivate a user

### Events (`/events`)

- `POST /events/` - Create a new event
- `GET /events/` - Get all events
- `GET /events/{event_id}` - Get a specific event
- `PUT /events/{event_id}` - Update an event
- `DELETE /events/{event_id}` - Delete an event
- `PATCH /events/{event_id}/close` - Close event registration

### Speakers (`/speakers`)

- `POST /speakers/` - Create a new speaker
- `GET /speakers/` - Get all speakers (includes 3 pre-loaded speakers)
- `GET /speakers/{speaker_id}` - Get a specific speaker
- `PUT /speakers/{speaker_id}` - Update a speaker
- `DELETE /speakers/{speaker_id}` - Delete a speaker

### Registrations (`/registrations`)

- `POST /registrations/` - Register a user for an event
- `GET /registrations/` - Get all registrations
- `GET /registrations/{registration_id}` - Get a specific registration
- `GET /registrations/user/{user_id}` - Get registrations by user
- `GET /registrations/event/{event_id}` - Get registrations by event
- `PATCH /registrations/{registration_id}/attend` - Mark attendance
- `PUT /registrations/{registration_id}` - Update a registration
- `DELETE /registrations/{registration_id}` - Delete a registration
- `GET /registrations/analytics/attendees` - Get users who attended events

### User Registration

- Only **active users** can register for events
- Users cannot register **more than once** for the same event
- Events must be **open** for registration
- Email addresses must be **unique**

### Event Management

- Events can be opened/closed for registration
- Event dates are validated
- Location is required for all events

### Attendance Tracking

- Registrations default to `attended: False`
- Attendance can be marked individually
- Analytics endpoint shows users who attended at least one event

## Data Models

### User

- `id`: Unique identifier
- `name`: Full name (1-100 characters)
- `email`: Valid email address (unique)
- `is_active`: Boolean flag (default: True)

### Event

- `id`: Unique identifier
- `title`: Event name (1-200 characters)
- `location`: Event location (1-200 characters)
- `date`: Event date
- `is_open`: Registration status (default: True)

### Speaker

- `id`: Unique identifier
- `name`: Speaker name (1-100 characters)
- `topic`: Presentation topic (1-200 characters)

### Registration

- `id`: Unique identifier
- `user_id`: Reference to user
- `event_id`: Reference to event
- `registration_date`: Timestamp of registration
- `attended`: Attendance status (default: False)

## Testing the API

### Example API Calls

1. **Create a User**

   ```bash
   curl -X POST "http://localhost:8000/users/" \
        -H "Content-Type: application/json" \
        -d '{"name": "Fatimah Olaitan", "email": "olusholaolaitan04@gmail.com"}'
   ```

2. **Create an Event**

   ```bash
   curl -X POST "http://localhost:8000/events/" \
        -H "Content-Type: application/json" \
        -d '{"title": "Tech Conference 2025", "location": "Lagos", "date": "2025-06-15"}'
   ```

3. **Register User for Event**

   ```bash
   curl -X POST "http://localhost:8000/registrations/" \
        -H "Content-Type: application/json" \
        -d '{"user_id": 1, "event_id": 1}'
   ```

4. **Mark Attendance**
   ```bash
   curl -X PATCH "http://localhost:8000/registrations/1/attend"
   ```

## Pre-loaded Data

The application starts with **3 speakers** already initialized:

- Dr. Sarah Johnson - "Machine Learning in Healthcare"
- Prof. Michael Chen - "Sustainable Software Architecture"
- Ms. Titilola Olaitan - "The Future of Web Development"

## Error Handling

The API returns appropriate HTTP status codes:

- `200` - Success
- `201` - Created
- `400` - Bad Request (validation errors)
- `404` - Not Found
- `500` - Internal server error
- `422` - Unprocessable Entity (Pydantic validation)

## Health Check

Check if the API is running:

```bash
curl http://localhost:8000/health
```

## Optional Features

- **Analytics Endpoint**: Track users who attended at least one event
- **Comprehensive Validation**: Email uniqueness, active user checks
- **Business Logic Enforcement**: Registration rules and constraints

---

**Developed for AltSchool of Backend Engineering Tinyuka 2024 Second Semester (Python) Project**
