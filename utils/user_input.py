from typing import Dict

class UserInputHandler:
    """Handles all user input and output interactions for direct AI recommendations"""
    
    def get_user_preferences(self) -> Dict[str, str]:
        """Collect user preferences including year and enhanced options"""
        print("\n" + "="*50)
        print("🎬 WELCOME TO THE AI MOVIE EXPERT!")
        print("="*50)
        
        preferences = {}
        
        questions = [
            ("year", "What year(s) are you interested in? (e.g., 2020, 1990s, 2010-2020, any)"),
            ("mood", "How are you feeling right now? (e.g., excited, relaxed, adventurous, thoughtful, romantic)"),
            ("genre", "What genre(s) do you usually enjoy? (e.g., action, comedy, drama, thriller, sci-fi)"),
            ("tone", "Do you want something light-hearted or more serious today?"),
            ("pace", "Do you prefer fast-paced action or slower, character-driven stories?"),
            ("time", "How much time do you have? (under 90min, 2-3 hours, doesn't matter)"),
            ("language", "Any preference for language/country? (Hollywood, international, anime, etc.)"),
            ("popularity", "Do you prefer popular blockbusters or hidden gems/indie films?"),
            ("actors", "Any favorite actors, directors, or specific movies you loved? (optional)")
        ]
        
        for key, question in questions:
            print(f"\n{question}")
            answer = input("➤ ").strip()
            preferences[key] = answer if answer else "no preference"
        
        return preferences
    
    def display_recommendations(self, recommendations: str):
        """Display AI recommendations to the user"""
        print("\n" + "🎯 YOUR PERSONALIZED MOVIE RECOMMENDATIONS ARE READY:")
        print("="*50)
        print(recommendations)
    
    def offer_movie_details(self, recommender):
        """Offer to provide additional details about recommended movies"""
        print("\n" + "="*50)
        while True:
            movie_query = input("Want details about any of these movies? (Enter movie name or 'quit'): ").strip()
            if movie_query.lower() in ['quit', 'exit', 'q', '']:
                break
            
            print(f"\n📖 Details for '{movie_query}':")
            print("-" * 40)
            details = recommender.get_movie_details(movie_query)
            print(details)
    
    def ask_for_new_recommendations(self) -> bool:
        """Ask if user wants new recommendations"""
        print("\n" + "="*50)
        again = input("Would you like new recommendations with different preferences? (y/n): ").strip().lower()
        return again in ['y', 'yes']
    
    def get_follow_up_preferences(self, initial_recommendations: str) -> str:
        """Get follow-up preferences based on initial recommendations"""
        print("\n" + "💬 QUICK FOLLOW-UP:")
        print("Based on these recommendations, I can refine further...")
        
        follow_ups = [
            "Do any of these sound appealing? (yes/no/maybe)",
            "Want something more similar to one of these, or completely different?",
            "Any specific decade you're gravitating toward after seeing these?",
            "Feeling more like a crowd-pleaser or something artsy/unique?"
        ]
        
        responses = []
        for question in follow_ups:
            print(f"\n{question}")
            answer = input("➤ ").strip()
            if answer:
                responses.append(f"{question} → {answer}")
        
        return " | ".join(responses)