from django.urls import path

from pypro.aperitivos.views import video_request, indice


app_name = 'aperitivos'

urlpatterns = [
    path('<slug:slug>', video_request, name='video'),
    path('', indice, name='indice'),

]