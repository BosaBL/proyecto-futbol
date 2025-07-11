from rest_framework import generics

from registro_futbol.models import Equipo, Jugador, Pais, Partido, Torneo

from .serializers import (
    EquipoSerializer,
    JugadorSerializer,
    PaisDetailSerializer,
    PartidoSerializer,
    TorneoSerializer,
)


class JugadorList(generics.ListAPIView):
    queryset = Jugador.objects.all().select_related("pais", "equipo", "equipo__pais")
    serializer_class = JugadorSerializer


class EquipoList(generics.ListAPIView):
    queryset = (
        Equipo.objects.select_related("pais")
        .prefetch_related("jugador_set__equipo__pais")
        .all()
    )
    serializer_class = EquipoSerializer


class TorneoList(generics.ListAPIView):
    serializer_class = TorneoSerializer

    def get_queryset(self):
        # NOTE: Realizar este prefetch_related mejora el rendimiento al evitar
        # consultas adicionales (N+1 queries problem).
        # Teniendo en cuenta como TorneoSerializer se comporta, se podría usar
        # annotated() para un rendimiento aún mejor, pero prefiero mantenerlo
        # sencillo, ya que mi principal objetivo es optimizar las queries a la
        # DB.
        return Torneo.objects.prefetch_related(
            "equipotorneo_set__equipo__jugador_set"
        ).all()


class PartidoList(generics.ListAPIView):
    queryset = Partido.objects.select_related(
        "equipo_local__pais",
        "equipo_visitante__pais",
        "torneo",
    ).all()
    serializer_class = PartidoSerializer


class PaisDetail(generics.RetrieveAPIView):
    serializer_class = PaisDetailSerializer

    def get_queryset(self):
        # NOTE: Evitar N+1 al hacer prefetch de todos los datos necesarios.
        return Pais.objects.prefetch_related(
            "equipo_set",
            "jugador_set",
            "torneo_set__equipotorneo_set__equipo__jugador_set",
        ).all()


class JugadorDetail(generics.RetrieveAPIView):
    queryset = Jugador.objects.select_related("pais", "equipo", "equipo__pais").all()
    serializer_class = JugadorSerializer


class EquipoDetail(generics.RetrieveAPIView):
    serializer_class = EquipoSerializer

    def get_queryset(self):
        # NOTE: Evitar N+1 al hacer prefetch de todos los datos necesarios.
        return Equipo.objects.prefetch_related("jugador_set").all()
