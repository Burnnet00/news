from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Artiles


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title','anons','ful_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'ful_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата статьи'
            }),

        }


