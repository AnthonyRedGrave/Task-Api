# Generated by Django 3.1.5 on 2021-01-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0013_auto_20210107_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.CharField(max_length=150, verbose_name='Размер файла'),
        ),
    ]