# Generated by Django 3.1.5 on 2021-01-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0012_auto_20210107_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='size_str',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.CharField(editable=False, max_length=150, verbose_name='Размер файла'),
        ),
    ]
