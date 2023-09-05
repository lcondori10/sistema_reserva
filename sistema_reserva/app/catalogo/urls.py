from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
]