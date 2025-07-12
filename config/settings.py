import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the application"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
    
    # IMDB Settings
    IMDB_BASE_URL = "https://www.imdb.com/search/title/"
    DEFAULT_YEAR = "2020"
    DEFAULT_LIMIT = 25
    
    # Request Headers
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # AI Settings
    AI_MODEL = "gpt-4o-mini"
    AI_MAX_TOKENS = 600
    AI_TEMPERATURE = 0.7
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
