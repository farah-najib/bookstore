import os
import django
django.setup()
from faker import Faker
from book_app.models import BookModel


# Set up Django environment



# Create a Faker instance
fake = Faker()

# Generate fake data for Book model
def generate_fake_books(num_books=20):
    for _ in range(num_books):
        title = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
        author = fake.name()
        description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
        price = fake.pydecimal(left_digits=3, right_digits=2, positive=True, min_value=10, max_value=1000)
        publication_date = fake.date_between(start_date='-10y', end_date='today')

        # Save book to database
        BookModel.objects.create(
            title=title,
            author=author,
            description=description,
            price=price,
            publication_date=publication_date
        )

if __name__ == '__main__':
    # Call the function to generate fake books
    generate_fake_books()
