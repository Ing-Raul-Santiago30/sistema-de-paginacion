from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="Inicio"),
    path('registro/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),


]    