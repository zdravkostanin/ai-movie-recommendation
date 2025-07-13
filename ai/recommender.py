from openai import OpenAI
from typing import List, Dict
from config.settings import Config

class AIRecommender:
    """Handles AI-powered movie recommendations"""
    
    def __init__(self):
        Config.validate_config()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.config = Config()
    
    def get_direct_recommendations(self, preferences: Dict[str, str]) -> str:
        """Get AI-powered movie recommendations using only user preferences"""
        prompt = self._create_direct_recommendation_prompt(preferences)
        
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
    
    def get_movie_details(self, movie_title: str, year: str = "") -> str:
        """Get detailed information about a specific movie"""
        query = f"{movie_title} {year}".strip()
        prompt = self._create_movie_details_prompt(query)
        
        try:
            response = self.client.chat.completions.create(
                model=self.config.AI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400,
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"❌ Error getting movie details: {str(e)}"
    
    def get_refined_recommendations(self, original_preferences: Dict[str, str], 
                                  initial_recommendations: str, 
                                  follow_up_responses: str) -> str:
        """Get refined recommendations based on user feedback"""
        prompt = self._create_refinement_prompt(
            original_preferences, initial_recommendations, follow_up_responses
        )
        
        try:
            response = self.client.chat.completions.create(
                model=self.config.AI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.config.AI_MAX_TOKENS,
                temperature=0.8  # Higher for more variety
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"❌ Error getting refined recommendations: {str(e)}"
    
    def _create_direct_recommendation_prompt(self, preferences: Dict[str, str]) -> str:
        """Create prompt for direct AI recommendations without movie list"""
        return f"""
You are an expert movie recommendation system with extensive knowledge of films from all eras, countries, and genres. Based on the user's preferences below, recommend exactly 3 movies that perfectly match their current mood and criteria.

USER PREFERENCES:
• Preferred year(s): {preferences.get('year', 'no preference')}
• Current mood: {preferences.get('mood', 'no preference')}
• Favorite genres: {preferences.get('genre', 'no preference')}
• Tone preference: {preferences.get('tone', 'no preference')}
• Pace preference: {preferences.get('pace', 'no preference')}
• Time available: {preferences.get('time', 'no preference')}
• Language/origin: {preferences.get('language', 'no preference')}
• Popularity level: {preferences.get('popularity', 'no preference')}
• Actors/directors/reference movies: {preferences.get('actors', 'no preference')}

INSTRUCTIONS:
1. Recommend exactly 3 movies that best match these preferences
2. Choose from your entire knowledge base - any movie from any year, country, or platform
3. Prioritize movies that match their specified year preference when possible
4. Consider their mood and time constraints carefully
5. Mix popular and lesser-known films based on their popularity preference
6. Include movies from different decades/styles if it fits their preferences

FORMAT YOUR RESPONSE AS:
🎬 **MOVIE 1: [Title] ([Year])**
- **Why this fits:** [Explain how it matches their mood, genre, and preferences]
- **What to expect:** [Brief description of tone, pace, and style]
- **Perfect if you:** [Specific reason this matches their current state]

🎬 **MOVIE 2: [Title] ([Year])**
- **Why this fits:** [Explanation]
- **What to expect:** [Description]
- **Perfect if you:** [Specific matching reason]

🎬 **MOVIE 3: [Title] ([Year])**
- **Why this fits:** [Explanation]
- **What to expect:** [Description]
- **Perfect if you:** [Specific matching reason]

**🎯 Quick Summary:** [One sentence explaining the common thread in your recommendations]

Make sure each recommendation is distinct and offers something different while still matching their preferences.
"""
    
    def _create_movie_details_prompt(self, movie_query: str) -> str:
        """Create prompt for getting movie details"""
        return f"""
Provide detailed information about the movie "{movie_query}":

1. **Plot Summary** (2-3 sentences, no spoilers)
2. **Key Details:** Director, main cast, runtime, rating
3. **Where to Watch:** Common streaming platforms or rental options
4. **Similar Movies:** 2-3 movies with similar vibes
5. **Fun Fact:** One interesting piece of trivia

Keep it concise but informative.
"""
    
    def _create_refinement_prompt(self, original_preferences: Dict[str, str], 
                                initial_recommendations: str, 
                                follow_up_responses: str) -> str:
        """Create prompt for refined recommendations"""
        return f"""
Based on the user's original preferences and their feedback to your initial recommendations, provide 3 NEW movie recommendations that better match what they're looking for.

ORIGINAL PREFERENCES:
{self._create_direct_recommendation_prompt(original_preferences)}

YOUR INITIAL RECOMMENDATIONS:
{initial_recommendations}

USER FEEDBACK:
{follow_up_responses}

Now provide 3 completely different movies that better align with their refined preferences. Use the same format as before but make sure these are different from your initial suggestions.
"""