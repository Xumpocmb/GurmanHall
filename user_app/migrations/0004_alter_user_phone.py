# Generated by Django 5.0.1 on 2024-02-12 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_user_date_joined_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='Телефон'),
        ),
    ]
