from django.conf.urls import url, include 
from django.urls import path 
from . import views 

#app_name='usuario' 

urlpatterns = [ 
    path('', views.home, name='home')
    #path('artistas/<alias>', views.detalle_artista, name="detalle-artista") 
] 