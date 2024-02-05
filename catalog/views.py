from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Book, BookInstance, Author


def index(request):
    # Словарь для передачи данных в шаблон
    text_head = 'На нашем сайте вы можете получить книги в электроном виде'
    # Данные об экземплярах книг в БД
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = "На складе")
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Данные об авторах книг
    authors = Author.objects
    num_authors = Author.objects.count()
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head, 'books': books, 'num_books': num_books, 'num_instances': num_instances,
               'num_instances_available': num_instances_available, 'authors': authors, 'num_authors': num_authors}
    # передача словаря context с данными в шаблон
    return render(request, 'index.html', context)
