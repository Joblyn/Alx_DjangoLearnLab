# Delete Operation

## Command

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by retrieving all books
all_books = Book.objects.all()
print(f"All books after deletion: {all_books}")
print(f"Number of books: {all_books.count()}")
```

## Expected Output

```
All books after deletion: <QuerySet []>
Number of books: 0
```

## Alternative Command (Direct delete)

```python
from bookshelf.models import Book

# Delete using QuerySet delete method
Book.objects.filter(title="Nineteen Eighty-Four").delete()

# Confirm deletion
all_books = Book.objects.all()
print(f"All books after deletion: {all_books}")
```

## Expected Output

```
All books after deletion: <QuerySet []>
```
