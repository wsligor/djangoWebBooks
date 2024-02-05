from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Словарь для передачи данных в шаблон
    text_head = 'Это заголовок главной страницы раздела Каталог'
    text_body = 'Это содержимое главной страницы раздела Каталог'
    context = {'text_head': text_head, 'text_body': text_body}
    # передача словаря context с данными в шаблон
    return render(request, 'index.html', context)
    # return HttpResponse("Главная страница каталога 'Мир книг'!!!'")
