# Generated by Django 5.0.1 on 2024-02-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0003_alter_order_email_alter_order_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
