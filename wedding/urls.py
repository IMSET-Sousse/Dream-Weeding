
from django.urls import path
from . import views

app_name = 'wedding'
urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
]