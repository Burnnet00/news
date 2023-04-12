from django.shortcuts import render


def index(reguest):
    return render(reguest, 'main/index.html')


def about(reguest):
    return render(reguest, 'main/about.html')


def cont(reguest):
    return render(reguest, 'main/cont.html')
