from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница!!',
        'test': 'text',
        'testing': ['1', '2','3']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
