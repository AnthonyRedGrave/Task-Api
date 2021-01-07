# Generated by Django 3.1.5 on 2021-01-07 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0010_auto_20210107_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['file_name'], 'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterModelOptions(
            name='fileinfo',
            options={'ordering': ['name'], 'verbose_name': 'Информация о файле', 'verbose_name_plural': 'Информация о файле'},
        ),
        migrations.AddField(
            model_name='file',
            name='file_name',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Название файла'),
        ),
        migrations.AddField(
            model_name='fileinfo',
            name='file',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fileinfo', to='files.file'),
        ),
    ]
