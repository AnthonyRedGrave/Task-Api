# Generated by Django 3.1.5 on 2021-01-28 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0032_advuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='advuser',
            name='email',
        ),
        migrations.AddField(
            model_name='advuser',
            name='max_size_of_files',
            field=models.IntegerField(default=50, verbose_name='Максимальный размер для хранения файлов'),
        ),
        migrations.AddField(
            model_name='advuser',
            name='phone',
            field=models.CharField(default=None, max_length=10, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advuser',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='adv_user', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advuser',
            name='user_name',
            field=models.CharField(default=None, max_length=150, verbose_name='Никнейм'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.advuser', verbose_name='Пользователь'),
        ),
    ]
