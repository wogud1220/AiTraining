from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:userNum>/", views.userNum, name="userNum"),
    path("gugu", views.gugugu, name="gugu"),
    path("bye", views.bye, name="bye"),
    path("bye2", views.bye2, name="bye2")
]