from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('corto', views.film, name='film'),
    path('instalacion', views.installation, name='installation'),
    path('creditos', views.credits, name='credits'),
    path('reserva', views.reservation, name='reservation'),
]