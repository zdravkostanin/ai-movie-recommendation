from ai.recommender import AIRecommender
from utils.user_input import UserInputHandler

def main():
    """Main entry point for the direct AI movie recommendation system"""
    print("\n" + "="*50)
    print("🎬 WELCOME TO THE AI MOVIE EXPERT!")
    print("="*50)

    # Initialize components
    recommender = AIRecommender()
    input_handler = UserInputHandler()
    
    try:
        # Get user's preferences
        preferences = input_handler.get_user_preferences()
        
        # Get AI recommendations
        print("\n🤖 Consulting AI movie expert...")
        recommendations = recommender.get_direct_recommendations(preferences)
        
        # Display results
        input_handler.display_recommendations(recommendations)
        
        # Offer movie details
        input_handler.offer_movie_details(recommender)
        
        # Ask for new recommendations
        while input_handler.ask_for_new_recommendations():
            recommendation_type = input_handler.get_recommendation_type()
            
            if recommendation_type == "refine":
                # Use follow-up questions to refine current recommendations
                follow_up_responses = input_handler.get_follow_up_preferences(recommendations)
                refined_recommendations = recommender.get_refined_recommendations(
                    preferences, recommendations, follow_up_responses
                )
                input_handler.display_recommendations(refined_recommendations)
            else:
                # Start completely fresh with new preferences
                new_preferences = input_handler.get_user_preferences()
                new_recommendations = recommender.get_direct_recommendations(new_preferences)
                input_handler.display_recommendations(new_recommendations)
            
    except KeyboardInterrupt:
        print("\n👋 Thanks for using the AI Movie Expert!")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()