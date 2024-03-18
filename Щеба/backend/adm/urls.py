from django.urls import path, re_path

from backend import settings
from django.conf.urls.static import static


from .views import *



urlpatterns = [
    path('', home, name="home"),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    #path('post/<slug:slug>/', Post_detail.as_view(), name='post_detail'),
    #re_path('post/<int:pk>/', AddComm, name='add_comm'),
    #re_path('post/<slug:slug>/', AddComm, name='add_comm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
