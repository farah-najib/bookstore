from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookModel (models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.title} {self.price}"

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portifolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username