from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    photo = models.ImageField(
        upload_to="photos",
        default=None, blank=True,
        null=True, verbose_name="Фото"
    )
    name = models.CharField('Наименование продукта', max_length = 200)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    def __str__(self):
        return self.name
    

class Comments(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'