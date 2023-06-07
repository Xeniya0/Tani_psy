from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная',
        'values': ['Some', 'body', 'was', 'told', 'me']
        }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html', {'title': 'Абоут'})

def picture(request):
    return render(request, 'main/picture.html', {'title': 'Пиктуре'})