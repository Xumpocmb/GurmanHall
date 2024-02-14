# Generated by Django 5.0.1 on 2024-02-14 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_emailverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('Шеф', 'Шеф'), ('Оператор', 'Оператор'), ('Курьер', 'Курьер'), ('Пользователь', 'Пользователь')], default='user', max_length=20, null=True, verbose_name='Роль'),
        ),
    ]
