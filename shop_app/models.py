from django.db import models


class ContactMessages(models.Model):
    name = models.CharField(max_length=25, null=True, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=False)
    phone = models.CharField(max_length=12, null=True, blank=True)
    message = models.TextField(max_length=1000, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Name: {self.name} | Email: {self.phone}'
