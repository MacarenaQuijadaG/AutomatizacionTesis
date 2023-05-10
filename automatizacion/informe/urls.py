from django.conf.urls import url, include 
from django.urls import path 
from . import views 


#app_name='informe' 

urlpatterns = [ 
    path('dashboard', views.dashboard, name='dashboard')
    #path('artistas/<alias>', views.detalle_artista, name="detalle-artista") 
] 