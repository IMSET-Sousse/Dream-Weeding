
from django.urls import path
from . import views

app_name = 'wedding'
urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
]
urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),
]