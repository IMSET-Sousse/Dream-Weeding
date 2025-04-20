from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('galerie/', views.galerie_view, name='galerie'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('articles/', views.liste_articles, name='liste_articles'),
]
