from dataclasses import dataclass
from typing import Optional

@dataclass
class Movie:
    """Data model for a movie"""
    title: str
    year: str
    genre: Optional[str] = None
    rating: Optional[str] = None
    description: Optional[str] = None

    def __str__(self):
        return f"{self.title}, ({self.year}) - {self.genre}"
    
    def to_dict(self):
        """Convert movie to dictionary for API calls"""
        return {
            'title': self.title,
            'year': self.year,
            'genre': self.genre or 'Unknown',
            'rating': self.rating or 'N/A',
            'description': self.description or 'No description available'
        }
    
    def format_for_ai(self):
        """Format movie information for AI prompts"""
        info = f"Title: {self.title}"
        if self.genre and self.genre != 'Unknown':
            info += f", Genre: {self.genre}"
        if self.rating and self.rating != 'N/A':
            info += f", Rating: {self.rating}"
        return info