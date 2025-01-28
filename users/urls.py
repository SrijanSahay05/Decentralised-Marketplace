from django.urls import path
from .views import signup, logout_view, login_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]