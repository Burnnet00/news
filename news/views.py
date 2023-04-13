from django.shortcuts import render, redirect

from .forms import ArtilesForm
from .models import Artiles

def news_home(request):
    news = Artiles.objects.order_by('-date')#all()
    return render(request, 'news/news_home.html',{'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error = 'Неверная форма'

    form = ArtilesForm
    data = {
        'form': form,
        'error' : error
    }
    return render(request, 'news/create.html', data)
