from django.shortcuts import render, get_object_or_404,redirect
from .models import BookModel
from .utils import search_books
from django.contrib.auth.decorators import login_required
from .models import ShoppingCart, CartItem
from .forms import AddToCartForm

def book_list(request):
    query = request.GET.get('q')
    books = search_books(query)
    return render(request, 'book_list.html', {'books': books, 'query': query})

def book_detail(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    return render(request, 'book_detail.html', {'book': book})




@login_required
def add_to_cart(request, book_id):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            book = BookModel.objects.get(pk=book_id)
            cart, created = ShoppingCart.objects.get_or_create(user=request.user)
            CartItem.objects.create(cart=cart, book=book, quantity=quantity)
            return redirect('view_cart')
    else:
        form = AddToCartForm()
    return render(request, 'add_to_cart.html', {'form': form})

@login_required
def view_cart(request):
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'view_cart.html', {'cart_items': cart_items})
