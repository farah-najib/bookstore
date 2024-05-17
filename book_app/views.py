from django.shortcuts import render, get_object_or_404
from .models import BookModel

def book_list(request):
    books = BookModel.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    return render(request, 'book_detail.html', {'book': book})
