import chromadb
from sentence_transformers import SentenceTransformer
import requests
from .models import Book

# LM Studio setup
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

# Embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# ChromaDB setup
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("books")

def index_books():
    """Index all books into ChromaDB"""
    books = Book.objects.all()
    
    for book in books:
        text = f"Title: {book.title}. Author: {book.author}. Description: {book.description or ''}"
        embedding = embedding_model.encode(text).tolist()
        
        collection.upsert(
            ids=[str(book.id)],
            embeddings=[embedding],
            metadatas=[{
                "title": book.title,
                "author": book.author,
                "book_id": book.id
            }],
            documents=[text]
        )
    
    return len(books)

def ask_question(question):
    """RAG: Ask question about books using LM Studio"""
    
    # Generate embedding for question
    question_embedding = embedding_model.encode(question).tolist()
    
    # Search similar books
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )
    
    # Build context
    context = "\n\n".join(results['documents'][0])
    
    # Prepare request payload
    payload = {
        "messages": [
            {"role": "system", "content": "You are a book expert. Answer based ONLY on the context provided."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ],
        "temperature": 0.7,
        "max_tokens": 300,
        "stream": False
    }
    
    # Call LM Studio
    try:
        response = requests.post(
            LM_STUDIO_URL,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            answer = result["choices"][0]["message"]["content"]
            return {
                "answer": answer,
                "sources": results['metadatas'][0]
            }
        else:
            return {
                "answer": f"LM Studio error: Please load model in Chat tab. Status: {response.status_code}",
                "sources": []
            }
    except Exception as e:
        return {
            "answer": f"Error: {str(e)}. Make sure LM Studio is running with model loaded.",
            "sources": []
        }