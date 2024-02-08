from django.urls import path
from . import views


urlpatterns = [
    path('books', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('', views.index, name='index')
]