from dataclasses import dataclass
from typing import Optional

@dataclass
class UserPreferences:
    """Data model for user preferences"""
    year: str
    mood: str
    genre: str
    tone: str
    pace: str
    time: str
    language: str
    popularity: str
    actors: str
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create UserPreferences from dictionary"""
        return cls(
            year=data.get('year', 'no preference'),
            mood=data.get('mood', 'no preference'),
            genre=data.get('genre', 'no preference'),
            tone=data.get('tone', 'no preference'),
            pace=data.get('pace', 'no preference'),
            time=data.get('time', 'no preference'),
            language=data.get('language', 'no preference'),
            popularity=data.get('popularity', 'no preference'),
            actors=data.get('actors', 'no preference')
        )