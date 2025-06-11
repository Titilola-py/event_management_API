from fastapi import FastAPI
from routes.events_routes import router as events_router
from routes.users_routes import router as users_router
from routes.speakers_routes import router as speakers_router
from routes.registrations_routes import router as registrations_router 

app = FastAPI(
    title="Event Management API",
    description="API for managing events, users, and speakers",
    version="1.0.0"
)

app.include_router(events_router, prefix="/events", tags=["events"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(speakers_router, prefix="/speakers", tags=["speakers"])
app.include_router(registrations_router, prefix="/registrations", tags=["registrations"])

@app.get("/")
async def root():
    return {"message": "Event Management API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)