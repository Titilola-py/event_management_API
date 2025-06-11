from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.speaker import Speaker, SpeakerCreate, SpeakerUpdate
from services import speaker_service

router = APIRouter()

@router.post("/", response_model=Speaker, status_code=status.HTTP_201_CREATED)
async def create_speaker(speaker_data: SpeakerCreate):
    """Create a new speaker"""
    speaker = speaker_service.create_speaker(speaker_data)
    return speaker

@router.get("/", response_model=List[Speaker])
async def get_all_speakers():
    """Get all speakers"""
    return speaker_service.get_all_speakers()

@router.get("/{speaker_id}", response_model=Speaker)
async def get_speaker(speaker_id: int):
    """Get a specific speaker by ID"""
    speaker = speaker_service.get_speaker(speaker_id)
    if not speaker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Speaker not found"
        )
    return speaker

@router.put("/{speaker_id}", response_model=Speaker)
async def update_speaker(speaker_id: int, speaker_data: SpeakerUpdate):
    """Update a speaker"""
    speaker = speaker_service.update_speaker(speaker_id, speaker_data)
    if not speaker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Speaker not found"
        )
    return speaker

@router.delete("/{speaker_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_speaker(speaker_id: int):
    """Delete a speaker"""
    if not speaker_service.delete_speaker(speaker_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Speaker not found"
        )