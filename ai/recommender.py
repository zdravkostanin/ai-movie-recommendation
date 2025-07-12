from openai import OpenAI
from typing import List, Dict
from models.movie import Movie
from config.settings import Config

class AIRecommender:
    """Handles AI-powered movie recommendations"""
    
    def __init__(self):
        Config.validate_config()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.config = Config()
    
    def get_recommendations(self, movies: List[Movie], preferences: Dict[str, str]) -> str:
        """Get AI-powered movie recommendations"""
        if not movies:
            return "❌ No movies available for recommendations."
        
        # Format movies for AI prompt
        movie_list = [movie.format_for_ai() for movie in movies]
        
        prompt = self._create_recommendation_prompt(preferences, movie_list)
        
        try:
            response = self.client.chat.completions.create(
                model=self.config.AI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.config.AI_MAX_TOKENS,
                temperature=self.config.AI_TEMPERATURE
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"❌ Error getting recommendation: {str(e)}"
    
    def _create_recommendation_prompt(self, preferences: Dict[str, str], movie_list: List[str]) -> str:
        """Create the AI prompt for recommendations"""
        return f"""
You are a movie recommendation expert. Based on the user's preferences and available movies, recommend the TOP 3 movies that best match their current mood and preferences.

USER PREFERENCES:
- Current mood: {preferences.get('mood', 'no preference')}
- Preferred genres: {preferences.get('genre', 'no preference')}
- Tone preference: {preferences.get('tone', 'no preference')}
- Pace preference: {preferences.get('pace', 'no preference')}
- Time available: {preferences.get('time', 'no preference')}
- Favorite actors/directors: {preferences.get('actors', 'no preference')}

AVAILABLE MOVIES:
{chr(10).join(movie_list)}

Please provide:
1. Your top 3 recommendations (ranked)
2. Brief explanation for each choice
3. Why each movie matches their current mood/preferences

Format your response clearly with numbered recommendations.
"""