from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('user/auth', views.auth, name='auth'),
    path('user/register', views.register, name='register'),
    path('user/signUp', views.signUp, name='signUp')
]