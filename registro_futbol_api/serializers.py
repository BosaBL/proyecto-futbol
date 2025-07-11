from rest_framework import serializers

from registro_futbol.models import Equipo, Jugador, Pais, Partido, Torneo


class PaisSerializer(serializers.ModelSerializer[Pais]):
    class Meta:  # pyright: ignore
        model = Pais
        fields = "__all__"


class JugadorSerializer(serializers.ModelSerializer[Jugador]):
    class Meta:  # pyright: ignore
        model = Jugador
        depth = 2
        fields = "__all__"


class EquipoSerializer(serializers.ModelSerializer[Equipo]):
    jugadores = JugadorSerializer(many=True, read_only=True, source="jugador_set")

    class Meta:  # pyright: ignore
        model = Equipo
        depth = 1
        fields = "__all__"


class SimpleEquipoSerializer(serializers.ModelSerializer[Equipo]):
    class Meta:  # pyright: ignore
        model = Equipo
        depth = 1
        fields = "__all__"


class EquipoEnTorneoSerializer(serializers.ModelSerializer[Equipo]):
    cantidad_jugadores = serializers.SerializerMethodField()

    class Meta:  # pyright: ignore
        depth = 1
        model = Equipo
        fields = "__all__"

    def get_cantidad_jugadores(self, obj):
        return obj.jugador_set.count()


class TorneoSerializer(serializers.ModelSerializer[Torneo]):
    equipos = serializers.SerializerMethodField()

    class Meta:  # pyright: ignore
        depth = 1
        model = Torneo
        fields = "__all__"

    def get_equipos(self, obj):
        equipos_en_torneo = obj.equipotorneo_set.all()
        equipos = [e.equipo for e in equipos_en_torneo]
        return EquipoEnTorneoSerializer(equipos, many=True).data


class SimpleTorneoSerializer(serializers.ModelSerializer[Torneo]):
    class Meta:  # pyright: ignore
        depth = 1
        model = Torneo
        fields = "__all__"


class PartidoSerializer(serializers.ModelSerializer[Partido]):
    equipo_local = SimpleEquipoSerializer(read_only=True)
    equipo_visitante = SimpleEquipoSerializer(read_only=True)
    torneo = SimpleTorneoSerializer(read_only=True)

    class Meta:  # pyright: ignore
        model = Partido
        fields = "__all__"


class PaisDetailSerializer(serializers.ModelSerializer[Pais]):
    equipos = SimpleEquipoSerializer(many=True, read_only=True, source="equipo_set")
    jugadores = JugadorSerializer(many=True, read_only=True, source="jugador_set")
    torneos = SimpleTorneoSerializer(many=True, read_only=True, source="torneo_set")

    class Meta:  # pyright: ignore
        model = Pais
        fields = "__all__"
