from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from books.rag import ask_question, index_books
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def ask_question_api(request):
    question = request.data.get('question')
    if not question:
        return Response({"error": "Question is required"}, status=400)
    try:
        result = ask_question(question)
        return Response({
            "answer": result.get("answer", "No answer"),
            "sources": result.get("sources", [])
        })
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
def index_books_api(request):
    count = index_books()
    return Response({"message": f"Indexed {count} books"})