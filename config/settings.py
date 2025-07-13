import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the direct AI recommendation application"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
    
    # AI Settings
    AI_MODEL = "gpt-4o-mini"
    AI_MAX_TOKENS = 800 
    AI_TEMPERATURE = 0.7
    
    # Movie Detail Settings
    DETAIL_MAX_TOKENS = 400
    DETAIL_TEMPERATURE = 0.3
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
