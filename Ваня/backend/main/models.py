from django.db import models

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