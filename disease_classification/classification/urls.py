from django.urls import path
from .views import user_login
from . import views
from .views import home

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', user_login, name='login'),
    path('', home, name='home'), 
]
