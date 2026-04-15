from django.core.management.base import BaseCommand
from books.scraper import scrape_books_from_website

class Command(BaseCommand):
    help = 'Scrape books from website'
    
    def handle(self, *args, **options):
        count = scrape_books_from_website()
        self.stdout.write(f"Successfully scraped {count} books")