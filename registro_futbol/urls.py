from django.urls import path

from . import views

urlpatterns = [
    path("", views.redirect_to_jugador, name="redirect_to_jugador"),
    # Equipo URLs
    path("equipos/", views.equipo_list, name="equipo_list"),
    path("equipos/crear/", views.equipo_create, name="equipo_create"),
    path("equipos/editar/<int:id>/", views.equipo_edit, name="equipo_edit"),
    path("equipos/eliminar/<int:id>/", views.equipo_delete, name="equipo_delete"),
    # Jugador URLs
    path("jugadores/", views.jugador_list, name="jugador_list"),
    path("jugadores/crear/", views.jugador_create, name="jugador_create"),
    path("jugadores/editar/<int:id>/", views.jugador_edit, name="jugador_edit"),
    path("jugadores/eliminar/<int:id>/", views.jugador_delete, name="jugador_delete"),
]
