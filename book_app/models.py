from django.db import models


# Create your models here.


from django.contrib.auth.models import User

#--------------------------------------------------------------------
class BookModel (models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publication_date = models.DateField()


    def __str__(self):
        return f"{self.title} {self.price}"
#-----------------------------------------------------------------------
class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
