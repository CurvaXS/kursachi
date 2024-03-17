from django.db import models
from django.utils import timezone
from django.urls import reverse

class Note(models.Model):
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    date = models.DateField(default=timezone.now)
    name = models.CharField('Наименование записи', max_length = 200)
    #slug = models.SlugField(max_length=250, unique=True , default='',)
    
    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'
        #index_together = (('id', 'slug'),)
    """
    def get_absolute_url(self):
        return reverse('adm:post_detail', args=[self.id, self.slug])
    """

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    note = models.ForeignKey(Note, related_name='comments', on_delete = models.PROTECT)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('created',)
        

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)