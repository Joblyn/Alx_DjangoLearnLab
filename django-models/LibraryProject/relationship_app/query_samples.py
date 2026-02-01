"""
Sample queries demonstrating Django ORM relationships.

This module contains sample queries for:
- ForeignKey relationships (Author -> Book)
- ManyToMany relationships (Library <-> Book)
- OneToOne relationships (Library <-> Librarian)
"""

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    
    This demonstrates the ForeignKey relationship between Book and Author.
    Using the related_name 'books', we can access all books for an author.
    
    Args:
        author_name (str): The name of the author to search for.
    
    Returns:
        QuerySet: All books by the specified author.
    """
    try:
        # Get the author by name
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author using objects.filter
        books = Book.objects.filter(author=author)
        
        print(f"Books by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
        
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def query_books_in_library(library_name):
    """
    List all books in a library.
    
    This demonstrates the ManyToMany relationship between Library and Book.
    Using the field 'books', we can access all books in a library.
    
    Args:
        library_name (str): The name of the library to search for.
    
    Returns:
        QuerySet: All books in the specified library.
    """
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        
        # Query all books in this library using the ManyToMany relationship
        books = library.books.all()
        
        print(f"Books in {library_name}:")
        for book in books:
            print(f"  - {book.title}")
        
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def query_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    
    This demonstrates the OneToOne relationship between Library and Librarian.
    Using the related_name 'librarian', we can access the librarian for a library.
    
    Args:
        library_name (str): The name of the library to search for.
    
    Returns:
        Librarian: The librarian for the specified library.
    """
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        
        # Query the librarian for this library using the OneToOne relationship
        librarian = library.librarian
        
        print(f"Librarian for {library_name}: {librarian.name}")
        
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None


# Example usage (uncomment to run):
# if __name__ == "__main__":
#     # Note: You need to have data in your database for these queries to return results.
#     # You can create sample data using Django shell or admin interface.
#     
#     # Query books by author
#     query_books_by_author("J.K. Rowling")
#     
#     # Query books in a library
#     query_books_in_library("Central Library")
#     
#     # Query librarian for a library
#     query_librarian_for_library("Central Library")
