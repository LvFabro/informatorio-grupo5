# En este urls.py se ubican todas las urls de la aplicacion 'blog'
# y son exportadas al urls.py de 'mi_sitio' .

# Imports
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('register/', views.registro, name='registro')
]