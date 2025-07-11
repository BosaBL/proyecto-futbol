from django import forms

from .models import Equipo, Jugador


class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre", "edad", "posicion", "pais", "equipo", "foto"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del jugador",
                }
            ),
            "edad": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese la edad",
                    "min": "16",
                    "max": "45",
                }
            ),
            "posicion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Delantero, Defensor, Mediocampista",
                }
            ),
            "pais": forms.Select(attrs={"class": "form-select"}),
            "equipo": forms.Select(attrs={"class": "form-select"}),
            "foto": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }
        labels = {
            "nombre": "Nombre del Jugador",
            "edad": "Edad",
            "posicion": "Posición",
            "pais": "País de Origen",
            "equipo": "Equipo",
            "foto": "Foto del Jugador",
        }


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre", "pais", "entrenador", "escudo"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del equipo",
                }
            ),
            "pais": forms.Select(attrs={"class": "form-select"}),
            "entrenador": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del entrenador",
                }
            ),
            "escudo": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }
        labels = {
            "nombre": "Nombre del Equipo",
            "pais": "País",
            "entrenador": "Entrenador",
            "escudo": "Escudo del Equipo",
        }
