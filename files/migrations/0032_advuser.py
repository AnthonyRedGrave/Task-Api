# Generated by Django 3.1.5 on 2021-01-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0031_remove_file_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Адрес электронной почты')),
            ],
        ),
    ]
