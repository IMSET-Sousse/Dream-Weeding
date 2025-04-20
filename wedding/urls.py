from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
]



from django.urls import path
from . import views
urlpatterns = [
    path('',views.liste_articles, name='liste_articles'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    # autres chemins
]
