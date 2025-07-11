from django.urls import path
from . import views

urlpatterns = [
    # Pais URLs
    path('paises/<int:pk>/', views.PaisDetail.as_view(), name='api_pais_detail'),

    # Equipo URLs
    path('equipos/', views.EquipoList.as_view(), name='api_equipo_list'),
    path('equipos/<int:pk>/', views.EquipoDetail.as_view(), name='api_equipo_detail'),

    # Torneo URLs
    path('torneos/', views.TorneoList.as_view(), name='api_torneo_list'),

    # Jugador URLs
    path('jugadores/', views.JugadorList.as_view(), name='api_jugador_list'),
    path('jugadores/<int:pk>/', views.JugadorDetail.as_view(), name='api_jugador_detail'),

    # Partido URLs
    path('partidos/', views.PartidoList.as_view(), name='api_partido_list'),
]
