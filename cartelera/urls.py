
from django.urls import path
from . import views

app_name = 'cartelera'


urlpatterns = [
path('', views.inicio, name='inicio'),
path('pelicula/<int:id>/', views.detalle_pelicula, name='detalle_pelicula'),
path('ticket/<str:codigo>/', views.ver_ticket, name='ver_ticket'),
]