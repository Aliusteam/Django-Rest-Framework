from django.contrib.auth.models import User
from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)  # Заголовок
    content = models.TextField(blank=True)  # Описание о женщинах
    time_create = models.DateTimeField(auto_now_add=True)  # Время создания записи
    time_update = models.DateTimeField(auto_now=True)  # Время изменения записи
    is_published = models.BooleanField(default=True)  # Опубликована или нет
    # cat - это ссылка на категорию (актриса, певица и тд)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # Название категории

    def __str__(self):
        return self.name
