from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:id>/', views.book_detail),
    path('ask/', views.ask_question_api),
    path('index/', views.index_books_api),
]