from django.db import models
from usersapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название проекта')
    link_to_repository = models.URLField(verbose_name='Ссылка на репозиторий', blank=True)
    user_set = models.ManyToManyField(User, verbose_name='Набор пользователей')

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text_note = models.CharField(max_length=256, verbose_name='Текст заметки', blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
