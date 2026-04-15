# AI-Powered Book Insight Platform

A full-stack web application with RAG (Retrieval-Augmented Generation) integration that processes book data and enables intelligent querying. Built as part of an internship assignment for Ergosphere Solutions.

## Features

- **Automated Book Scraping** - Collects book data from websites using Selenium & BeautifulSoup
- **RAG Pipeline** - ChromaDB vector database with sentence-transformers embeddings
- **REST APIs** - Django REST Framework endpoints for book listing and Q&A
- **Admin Panel** - Django admin interface for managing books
- **Responsive Frontend** - ReactJS with Tailwind CSS

## Tech Stack

| Layer | Technology |
| Backend | Django REST Framework |
| Database | SQLite + ChromaDB |
| AI/ML | Sentence Transformers (all-MiniLM-L6-v2) |
| Frontend | ReactJS + Tailwind CSS |
| Automation | Selenium, BeautifulSoup4 |

## Prerequisites

- Python 3.9+
- Node.js (for frontend)

## Installation

### Backend Setup

```bash
# Clone repository
git clone https://github.com/qanoot-iftekhar/book-insight-platform.git
cd book-insight-platform

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Frontend Setup

```bash
cd frontend
npm install
npm start
```

API Endpoints

Endpoint Method Description
/api/books/ GET List all books
/api/books/{id}/ GET Get book details
/api/ask/ POST Ask question about books (RAG)
/api/index/ POST Index books to ChromaDB
/admin/ GET Django admin panel

RAG Pipeline

The system implements a complete RAG pipeline:

1. Embedding Generation - Sentence Transformers (all-MiniLM-L6-v2)
2. Vector Storage - ChromaDB for similarity search
3. Context Retrieval - Semantic search across book chunks
4. Answer Generation - Context-aware responses (LM Studio / OpenAI ready)

Screenshots

Admin Panel

screenshort/admin-books.jpg

API Response

screenshort/api-response.jpg

Frontend UI

screenshort/frontend-ui.jpg

Project Structure

screenshort/project-structure.jpg

Sample Q&A

Question: "Suggest a good book"

Response: Based on our database, "The Great Gatsby" by F. Scott Fitzgerald (Rating: 4.5/5) is highly recommended.

Author

Submitted as part of internship assignment for Ergosphere Solutions

## Submission Date

**Submitted** April 15, 2026  
**Deadline** April 18, 2026  
*Early submission preference claimed*
