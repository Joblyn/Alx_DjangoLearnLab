# Update Operation

## Command

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

print(f"Updated book title: {book.title}")
```

## Expected Output

```
Updated book title: Nineteen Eighty-Four
```

## Alternative Command (Using update method)

```python
from bookshelf.models import Book

# Update using QuerySet update method
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")

# Retrieve and verify
book = Book.objects.get(title="Nineteen Eighty-Four")
print(f"Updated book title: {book.title}")
```

## Expected Output

```
Updated book title: Nineteen Eighty-Four
```
