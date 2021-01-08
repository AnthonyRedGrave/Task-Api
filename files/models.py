from django.db import models
import os
from time import time
import datetime
from django.conf import settings
from django.contrib.auth.models import User


class File(models.Model):
    name = models.CharField("Название файла", max_length=150, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True, null = True)
    file = models.FileField("Файл", upload_to="files/%Y/%m/%d/", blank=True, null=True)
    content = models.CharField("Описание для файла", blank=True, null=True, default="Нет описания", max_length=200)
    date_pub = models.DateTimeField("Дата публикации файла", auto_now_add=True)
    slug = models.SlugField("Слаг", blank=True, null=True, max_length=70)
    size = models.CharField("Размер файла", max_length=150, blank=True, null=True)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        name = self.file.name
        super().save(*args, **kwargs)#предварительное сохранение
        if self.file:
            fullpath = os.path.join(settings.MEDIA_ROOT, self.file.field.upload_to, self.file.path)
            self.slug = os.path.join(settings.MEDIA_ROOT, self.file.name)

            self.size = os.path.getsize(fullpath)
        else:
            self.file = None
        if not self.name:
            self.name = name
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(self.file.path)
        print(self.file.path)
        super().delete(*args, **kwargs)



    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        ordering = ['name']




