"""
URL configuration for relationship_app.

This module defines URL patterns for:
- Function-based view: list_books
- Class-based view: LibraryDetailView
- Authentication views: login, logout, register
"""

from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout

urlpatterns = [
    # Function-based view to list all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
