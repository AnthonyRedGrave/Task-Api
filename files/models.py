from django.db import models
import os
from time import time
import datetime
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.template.defaultfilters import filesizeformat
from django.db.models.signals import post_init
from django.dispatch.dispatcher import receiver


class AdvUser(models.Model):
    user_name = models.CharField("Никнейм", max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='adv_user')
    phone = models.CharField('Телефон', max_length=10)
    max_size_of_files = models.IntegerField('Максимальный размер для хранения файлов (в байтах)', default=104857600, editable=False)
    correct_max_size_of_files = models.CharField('Максимальный размер для хранения файлов', max_length=150,
                                                 editable=False, default=0)
    engaged_size = models.IntegerField('Занято места (в байтах)', default=0, editable=False)
    correct_engaged_size = models.CharField('Занято места', max_length=150, editable=False, default=0)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

@receiver(post_init, sender = AdvUser)
def advuser_post_save(sender, instance, *args, **kwargs):
    instance.correct_max_size_of_files = filesizeformat(instance.max_size_of_files)



class File(models.Model):
    name = models.CharField("Название файла", max_length=150, blank=True, null=True)
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name="Пользователь", blank = True, null = True,
                             related_name='file')
    file = models.FileField("Файл", upload_to="files/%Y/%m/%d/", blank=True, null=True)
    content = models.CharField("Описание для файла", blank=True, null=True, default="Нет описания", max_length=200)
    date_pub = models.DateTimeField("Дата публикации файла", auto_now_add=True)
    slug = models.SlugField("Слаг", blank=True, null=True, max_length=70)
    size = models.IntegerField("Размер файла (в байтах)", editable=False, blank=True, null=True)
    correct_size = models.CharField("Размер файла", max_length=150, blank=True, null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        name = self.file.name
        super().save(*args, **kwargs)#предварительное сохранение
        if self.file:
            print("сохранение с файлом")
            fullpath = os.path.join(settings.MEDIA_ROOT, self.file.field.upload_to, self.file.path)
            self.slug = os.path.join(settings.MEDIA_ROOT, self.file.name)
            self.size = os.path.getsize(fullpath)
            self.correct_size = filesizeformat(self.size)
        else:
            self.file = None
        if not self.name:
            self.name = name
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.file:
            os.remove(self.file.path)
            print(self.file.path)
        super().delete(*args, **kwargs)



    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        ordering = ['-date_pub']




