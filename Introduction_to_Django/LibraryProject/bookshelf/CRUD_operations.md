# CRUD Operations - Django Shell

This document contains all the CRUD (Create, Read, Update, Delete) operations performed on the Book model using Django's ORM through the Django shell.

## Prerequisites

Before running these commands, ensure you:

1. Have created the `bookshelf` app
2. Have defined the `Book` model with title, author, and publication_year fields
3. Have run migrations: `python manage.py makemigrations` and `python manage.py migrate`
4. Open Django shell: `python manage.py shell`

---

## 1. CREATE Operation

### Command:

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book}")
```

### Expected Output:

```
Book created: 1984
```

### Alternative Method:

```python
from bookshelf.models import Book

# Create a Book instance using save()
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book created: {book}")
```

---

## 2. RETRIEVE Operation

### Command:

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

### Expected Output:

```
All books: <QuerySet [<Book: 1984>]>

Book Details:
Title: 1984
Author: George Orwell
Publication Year: 1949
```

### Alternative Retrieve Method:

```python
from bookshelf.models import Book

# Retrieve using filter
book = Book.objects.filter(title="1984").first()
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
```

### Expected Output:

```
Title: 1984, Author: George Orwell, Year: 1949
```

---

## 3. UPDATE Operation

### Command:

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

print(f"Updated book title: {book.title}")
```

### Expected Output:

```
Updated book title: Nineteen Eighty-Four
```

### Alternative Update Method:

```python
from bookshelf.models import Book

# Update using QuerySet update method
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")

# Retrieve and verify
book = Book.objects.get(title="Nineteen Eighty-Four")
print(f"Updated book title: {book.title}")
```

### Expected Output:

```
Updated book title: Nineteen Eighty-Four
```

---

## 4. DELETE Operation

### Command:

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

### Expected Output:

```
All books after deletion: <QuerySet []>
Number of books: 0
```

### Alternative Delete Method:

```python
from bookshelf.models import Book

# Delete using QuerySet delete method
Book.objects.filter(title="Nineteen Eighty-Four").delete()

# Confirm deletion
all_books = Book.objects.all()
print(f"All books after deletion: {all_books}")
```

### Expected Output:

```
All books after deletion: <QuerySet []>
```

---

## Summary

These CRUD operations demonstrate:

- **Create**: Using `objects.create()` or instantiating and calling `save()`
- **Retrieve**: Using `objects.all()`, `objects.get()`, or `objects.filter()`
- **Update**: Modifying attributes and calling `save()`, or using `objects.update()`
- **Delete**: Using `delete()` on an instance or on a QuerySet

All operations were performed successfully on the Book model with the following structure:

- `title`: CharField (max_length=200)
- `author`: CharField (max_length=100)
- `publication_year`: IntegerField
