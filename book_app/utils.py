from django.db.models import Q
from .models import BookModel

def search_books(query=None):
    if query:
        return BookModel.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )
    return BookModel.objects.all()
