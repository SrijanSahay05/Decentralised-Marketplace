from django.urls import path
from .views import index, about, sell, buy

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('sell/', sell, name='sell'),
    path('buy/', buy, name='buy'),
]