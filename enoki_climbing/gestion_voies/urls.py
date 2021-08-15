from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = 'gestion_voies'
urlpatterns = [
    path('', views.liste_annonces, name='index'),#url de l'index
    path('voie/', views.liste_annonces, name='index'),#url de l'index
    path('formulaire', views.formulaire, name='formaulaire'),#url de l'index
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)