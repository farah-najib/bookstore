from django.shortcuts import render, get_object_or_404
from .models import BookModel
from .utils import search_books

def book_list(request):
    query = request.GET.get('q')
    books = search_books(query)
    return render(request, 'book_list.html', {'books': books, 'query': query})

def book_detail(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    return render(request, 'book_detail.html', {'book': book})
