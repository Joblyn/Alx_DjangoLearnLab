# Retrieve Operation

## Command

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
print(f"All books: {books}")

# Retrieve the specific book by title
book = Book.objects.get(title="1984")
print(f"\nBook Details:")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

## Expected Output

```
All books: <QuerySet [<Book: 1984>]>

Book Details:
Title: 1984
Author: George Orwell
Publication Year: 1949
```

## Alternative Command (Filter)

```python
from bookshelf.models import Book

# Retrieve using filter
book = Book.objects.filter(title="1984").first()
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
```

## Expected Output

```
Title: 1984, Author: George Orwell, Year: 1949
```
