from django.db import models

# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название проекта')
    # field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, verbose_name='Фото проекта')
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='images/', default=None, verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

