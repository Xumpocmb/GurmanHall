# Generated by Django 5.0.1 on 2024-02-12 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0005_alter_category_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('sauce', models.CharField(blank=True, max_length=350, null=True, verbose_name='Соус для запеченных роллов')),
                ('description', models.CharField(blank=True, max_length=350, null=True, verbose_name='Комментарий')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]