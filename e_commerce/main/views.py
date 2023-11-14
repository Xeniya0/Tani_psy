from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная'})

def about(request):
    return render(request, 'main/about.html', {'title': 'Обо мне'})

def price(request):
    return render(request, 'main/price.html', {'title': 'Цены'})

def blog(request):
    return render(request, 'main/blog.html', {'title': 'Блог'})

def faq(request):
    return render(request, 'main/faq.html', {'title': 'FAQ'})

def review(request):
    return render(request, 'main/review.html', {'title': 'Отзывы'})

def dogovor(request):
    return render(request, 'main/dogovor.html', {'title': 'Договор'})

def contacts(request):
    return render(request, 'main/contacts.html', {'title': 'Контакты'})
