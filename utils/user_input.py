from typing import Dict

class UserInputHandler:
    """Handles all user input and output interactions"""
    
    def get_year_preference(self) -> str:
        """Get user's preferred year for movie recommendations"""
        year = input("What year of movies would you like to explore? (default: 2020): ").strip()
        return year if year else "2020"
    
    def get_user_preferences(self) -> Dict[str, str]:
        """Collect user preferences through interactive prompts"""
        
        preferences = {}
        
        questions = [
            ("mood", "How are you feeling right now? (e.g., excited, relaxed, adventurous, thoughtful, romantic)"),
            ("genre", "What genre(s) do you usually enjoy? (e.g., action, comedy, drama, thriller, sci-fi)"),
            ("tone", "Do you want something light-hearted or more serious today?"),
            ("pace", "Do you prefer fast-paced action or slower, character-driven stories?"),
            ("time", "How much time do you have? (quick watch under 2hrs, or willing to commit to longer?)"),
            ("actors", "Any favorite actors or directors? (optional - just press enter to skip)")
        ]
        
        for key, question in questions:
            print(f"\n{question}")
            answer = input("➤ ").strip()
            preferences[key] = answer if answer else "no preference"
        
        return preferences
    
    def display_recommendations(self, recommendations: str):
        """Display AI recommendations to the user"""
        print("\n" + "🎯 YOUR PERSONALIZED MOVIE RECOMMENDATIONS:")
        print("="*50)
        print(recommendations)
    
    def ask_for_new_recommendations(self) -> bool:
        """Ask if user wants new recommendations"""
        print("\n" + "="*50)
        again = input("Would you like to get new recommendations with different preferences? (y/n): ").strip().lower()
        return again in ['y', 'yes']