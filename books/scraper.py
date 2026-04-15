import requests
from bs4 import BeautifulSoup
from .models import Book

def scrape_books_from_website():
    """Example: Scrape books from a sample website"""
    
    # Example website for testing (Goodreads alternative)
    url = "https://books.toscrape.com/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books_data = []
    
    for book in soup.select('article.product_pod')[:10]:  # 10 books
        title = book.select_one('h3 a')['title']
        price = book.select_one('.price_color').text
        rating = book.select_one('p.star-rating')['class'][1]
        
        # Rating mapping
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        
        book_obj = Book(
            title=title,
            author="Unknown",  # Website doesn't show author
            rating=rating_map.get(rating, 3),
            description=f"Price: {price}",
            book_url=url,
            genre="General"
        )
        books_data.append(book_obj)
    
    # Save to database
    Book.objects.bulk_create(books_data)
    return len(books_data)