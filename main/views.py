from django.shortcuts import render


def index(reguest):
    data = {
        'title': 'Главная страничка'
    }
    return render(reguest, 'main/index.html', data)


def about(reguest):
    return render(reguest, 'main/about.html')


def cont(reguest):
    return render(reguest, 'main/cont.html')
