from django.urls import path

from pypro.aperitivos.views import video

app_name = 'Aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]