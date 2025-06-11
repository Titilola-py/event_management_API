from fastapi import FastAPI
from routes import events_routes, registrations_routes, speakers_routes, users_routes

app = FastAPI(
    title="Event Management API",
description="A system for managing events, users, speakers and registrations",
version="1.0.0"
)

app.include_router(users_routes.router, prefix="/users", tags=["users"])
app.include_router(events_routes.router, prefix="/events", tags=["events"])
app.include_router(speakers_routes.router, prefix="/speakers", tags=["speakers"])
app.include_router(registrations_routes.router, prefix="/registrations", tags=["registrations"])

@app.get("/")
async def root():
    return {"message": "Welcome to Event Management API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
#http://127.0.0.1:8000 ==> http://localhost:8000