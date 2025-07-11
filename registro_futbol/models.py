from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Pais(models.Model):

    nombre = models.CharField(max_length=100, help_text="Nombre del país")

    def __str__(self):
        return self.nombre


class Equipo(models.Model):

    nombre = models.CharField(max_length=100, help_text="Nombre del equipo")
    pais = models.ForeignKey(
        Pais, on_delete=models.CASCADE, help_text="País al que pertenece el equipo"
    )
    entrenador = models.CharField(max_length=100, help_text="Nombre del entrenador")
    escudo = models.ImageField(upload_to="escudos/", help_text="Escudo del equipo")

    def __str__(self):
        return self.nombre


class Torneo(models.Model):

    nombre = models.CharField(max_length=100, help_text="Nombre del torneo")
    pais = models.ForeignKey(
        Pais, on_delete=models.CASCADE, help_text="País en el que se juega el torneo"
    )

    def __str__(self):
        return self.nombre


class EquipoTorneo(models.Model):

    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("equipo", "torneo")

    def __str__(self):
        return f"{self.equipo} en {self.torneo}"


class Jugador(models.Model):

    nombre = models.CharField(max_length=100, help_text="Nombre del jugador")
    edad = models.IntegerField(
        help_text="Edad del jugador",
        validators=[MaxValueValidator(46), MinValueValidator(16)],
    )
    posicion = models.CharField(
        max_length=100, help_text="Posición en la que juega el jugador"
    )
    pais = models.ForeignKey(
        Pais, on_delete=models.CASCADE, help_text="País de origen del jugador"
    )
    equipo = models.ForeignKey(
        Equipo, on_delete=models.CASCADE, help_text="Equipo en el que juega el jugador"
    )
    foto = models.ImageField(upload_to="fotos/", help_text="Foto del jugador")

    def __str__(self):
        return self.nombre


class Partido(models.Model):

    fecha = models.DateField(help_text="Fecha del partido")
    equipo_local = models.ForeignKey(
        Equipo, related_name="partidos_local", on_delete=models.CASCADE
    )
    equipo_visitante = models.ForeignKey(
        Equipo, related_name="partidos_visitante", on_delete=models.CASCADE
    )
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    goles_local = models.IntegerField(default=0, help_text="Goles del equipo local")
    goles_visitante = models.IntegerField(
        default=0, help_text="Goles del equipo visitante"
    )

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} ({self.fecha}) - {self.torneo}"
