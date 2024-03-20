from django.urls import path, re_path

from backend import settings
from django.conf.urls.static import static


from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('catalog/', catalog, name="catalog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
