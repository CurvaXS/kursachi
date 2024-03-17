from django.urls import path, re_path

from backend import settings
from django.conf.urls.static import static


from .views import *



urlpatterns = [
    path('', home, name="home"),
    path('post/<int:id>/', post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
