import requests
from bs4 import BeautifulSoup
from typing import List
from models.movie import Movie
from config.settings import Config

class IMDBScraper:
    """Handles scraping movie data from IMDB"""
    
    def __init__(self):
        self.config = Config()
    
    def scrape_movies(self, year: str = None, limit: int = 25) -> List[Movie]:
        """Scrape movies from IMDB for a given year"""
        year = year or self.config.DEFAULT_YEAR
        url = f"{self.config.IMDB_BASE_URL}?release_date={year},{year}&title_type=feature&sort=num_votes,desc"
        
        try:
            response = requests.get(url, headers=self.config.HEADERS)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, "lxml")
            movie_divs = soup.find_all('div', attrs={'class': 'ipc-metadata-list-summary-item__c'})
            
            movies = []
            for i, div_item in enumerate(movie_divs[:limit]):
                movie = self._extract_movie_data(div_item, year)
                if movie:
                    movies.append(movie)
                    print(f"{i+1}. {movie.title}")
            
            print(f"\n✅ Successfully scraped {len(movies)} movies!")
            return movies
            
        except requests.RequestException as e:
            print(f"❌ Error scraping IMDB: {str(e)}")
            return []
    
    def _extract_movie_data(self, div_item, year: str) -> Movie:
        """Extract movie data from a BeautifulSoup div element"""
        # Extract title
        title_link = div_item.find('a', href=lambda x: x and 'sr_t_' in x)
        if not title_link:
            return None
        
        full_text = title_link.get_text(strip=True)
        title = full_text.split('. ', 1)[-1] if '. ' in full_text else full_text
        
        # Extract additional data
        genre = self._extract_genre(div_item)
        rating = self._extract_rating(div_item)
        description = self._extract_description(div_item)
        
        return Movie(
            title=title,
            year=year,
            genre=genre,
            rating=rating,
            description=description
        )
    
    def _extract_genre(self, div_item) -> str:
        """Extract genre from movie div"""
        genre_elements = div_item.find_all('span', class_='ipc-metadata-list-summary-item__li')
        genres = []
        
        common_genres = ['action', 'comedy', 'drama', 'thriller', 'horror', 'romance', 'sci-fi', 'fantasy', 'adventure', 'crime']
        
        for element in genre_elements:
            text = element.get_text(strip=True)
            if any(genre in text.lower() for genre in common_genres):
                genres.append(text)
        
        return ', '.join(genres) if genres else 'Unknown'
    
    def _extract_rating(self, div_item) -> str:
        """Extract IMDB rating"""
        rating_element = div_item.find('span', class_='ipc-rating-star')
        return rating_element.get_text(strip=True) if rating_element else 'N/A'
    
    def _extract_description(self, div_item) -> str:
        """Extract movie description"""
        desc_element = div_item.find('div', class_='ipc-html-content-inner-div')
        return desc_element.get_text(strip=True) if desc_element else 'No description available'