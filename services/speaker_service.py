from typing import Dict, List, Optional
from schemas.speaker_schema import Speaker, SpeakerCreate, SpeakerUpdate

speakers_db: Dict[int, Speaker] = {}
speaker_id_counter = 1

def initialize_speakers():
    """Initialize the app with 3 speakers as required"""
    global speaker_id_counter

    initial_speakers = [
        {"name": "Dr. Sarah Johnson", "topic": "Machine Learning in Healthcare"},
        {"name": "Prof. Michael Chen", "topic": "Sustainable Software Architecture"},
        {"name": "Ms. Titilola Olaitan", "topic": "The Future of Web Development"}
    ] 

    for speaker_data in initial_speakers:
        speaker = Speaker(
            id=speaker_id_counter,
            name=speaker_data["name"],
            topic=speaker_data["topic"]
        )
        speakers_db[speaker_id_counter] = speaker
        speaker_id_counter += 1

def create_speaker(speaker_data: SpeakerCreate) -> Speaker:
    global speaker_id_counter

    speaker = Speaker(
        id=speaker_id_counter,
        name=speaker_data.name,
        topic=speaker_data.topic
    )
    speakers_db[speaker_id_counter] = speaker
    speaker_id_counter += 1
    return speaker

def get_speaker(speaker_id: int) -> Optional[Speaker]:
    return speakers_db.get(speaker_id)

def get_all_speakers() -> List[Speaker]:
    return list(speakers_db.values())

def _update_speaker(speaker_id: int, speaker_data: SpeakerUpdate) -> Optional[Speaker]:
    if speaker_id not in speakers_db:
        return None
    
    speaker = speakers_db[speaker_id]
    update_data = speaker_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(speaker, field, value)

    return speaker

def delete_speaker(speaker_id: int) -> bool:
    if speaker_id in speakers_db:
        del speakers_db[speaker_id]
        return True
    return False

initialize_speakers()    