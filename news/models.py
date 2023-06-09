from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название', max_length=150)
    anons = models.CharField('Aнонс', max_length=255)
    ful_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def det_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'