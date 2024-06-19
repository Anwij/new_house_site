from django.db import models

# Create your models here.


class Application(models.Model):
    email = models.EmailField(max_length=255, verbose_name='Email')
    content = models.TextField(verbose_name='Описание заявки')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
