from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path('Register', views.register, name='register'),
    path("Recommend", views.Recommend, name="recommend"),


]

 