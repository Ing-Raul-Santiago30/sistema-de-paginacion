from django.urls import path
import views


urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="Inicio"),
]