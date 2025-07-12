from scrapers.imdb_scraper import IMDBScraper
from ai.recommender import AIRecommender
from utils.user_input import UserInputHandler

def main():
    """Main entry point for the movie recommendation system"""
    print("🎬 Welcome to the AI Movie Recommendation System!")
    
    # Initialize components
    scraper = IMDBScraper()
    recommender = AIRecommender()
    input_handler = UserInputHandler()
    
    try:
        # Get user's year preference
        year = input_handler.get_year_preference()
        
        # Scrape movies
        print(f"\nScraping movies from {year}...")
        movies = scraper.scrape_movies(year, limit=25)
        
        if not movies:
            print("❌ No movies found. Please try again.")
            return
        
        # Get user preferences
        preferences = input_handler.get_user_preferences()
        
        # Get AI recommendations
        print("\n🤖 Generating recommendations...")
        recommendations = recommender.get_recommendations(movies, preferences)
        
        # Display results
        input_handler.display_recommendations(recommendations)
        
        # Ask for new recommendations
        if input_handler.ask_for_new_recommendations():
            new_preferences = input_handler.get_user_preferences()
            new_recommendations = recommender.get_recommendations(movies, new_preferences)
            input_handler.display_recommendations(new_recommendations)
            
    except KeyboardInterrupt:
        print("\n👋 Thanks for using the movie recommender!")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()