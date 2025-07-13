from ai.recommender import AIRecommender
from utils.user_input import UserInputHandler

def main():
    """Main entry point for the direct AI movie recommendation system"""
    
    # Initialize components
    recommender = AIRecommender()
    input_handler = UserInputHandler()
    
    try:
        # Get user preferences (including year)
        preferences = input_handler.get_user_preferences()
        
        # Get AI recommendations directly (no movie list needed)
        print("\n🤖 Consulting AI movie expert...")
        recommendations = recommender.get_direct_recommendations(preferences)
        
        # Display results
        input_handler.display_recommendations(recommendations)
        
        # Offer movie details
        input_handler.offer_movie_details(recommender)
        
        # Ask for new recommendations
        if input_handler.ask_for_new_recommendations():
            new_preferences = input_handler.get_user_preferences()
            new_recommendations = recommender.get_direct_recommendations(new_preferences)
            input_handler.display_recommendations(new_recommendations)
            
    except KeyboardInterrupt:
        print("\n👋 Thanks for using the AI Movie Expert!")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()