from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EquipoForm, JugadorForm
from .models import Equipo, Jugador


def redirect_to_jugador(request):
    return redirect("jugador_list")


# Vistas de Equipo


def equipo_list(request):
    """
    Vista para listar todos los equipos.
    """
    equipos = Equipo.objects.all()
    return render(request, "registro_futbol/equipo_list.html", {"equipos": equipos})


def equipo_create(request):
    """
    Vista para crear un nuevo equipo.
    """
    if request.method == "POST":
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Equipo "{form.cleaned_data["nombre"]}" creado correctamente.',
            )
            return redirect("equipo_list")
    else:
        form = EquipoForm()
    return render(request, "registro_futbol/equipo_form.html", {"form": form})


def equipo_edit(request, id):
    """
    Vista para editar un equipo existente.
    """
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == "POST":
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Equipo "{form.cleaned_data["nombre"]}" actualizado correctamente.',
            )
            return redirect("equipo_list")
    else:
        form = EquipoForm(instance=equipo)
    return render(request, "registro_futbol/equipo_form.html", {"form": form})


def equipo_delete(request, id):
    """
    Vista para eliminar un equipo.
    """
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == "POST":
        name = equipo.nombre
        equipo.delete()
        messages.success(request, f'Equipo "{name}" eliminado correctamente.')
        return redirect("equipo_list")
    return render(
        request, "registro_futbol/equipo_confirm_delete.html", {"equipo": equipo}
    )


# Vistas de Jugador


def jugador_list(request):
    """
    Vista para listar todos los jugadores.
    """
    jugadores = Jugador.objects.all()
    return render(
        request, "registro_futbol/jugador_list.html", {"jugadores": jugadores}
    )


def jugador_create(request):
    """
    Vista para crear un nuevo jugador.
    """
    if request.method == "POST":
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Jugador "{form.cleaned_data["nombre"]}" creado correctamente.',
            )
            return redirect("jugador_list")
    else:
        form = JugadorForm()
    return render(request, "registro_futbol/jugador_form.html", {"form": form})


def jugador_edit(request, id):
    """
    Vista para editar un jugador existente.
    """
    jugador = get_object_or_404(Jugador, id=id)
    if request.method == "POST":
        form = JugadorForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Jugador "{form.cleaned_data["nombre"]}" actualizado correctamente.',
            )
            return redirect("jugador_list")
    else:
        form = JugadorForm(instance=jugador)
    return render(request, "registro_futbol/jugador_form.html", {"form": form})


def jugador_delete(request, id):
    """
    Vista para eliminar un jugador.
    """
    jugador = get_object_or_404(Jugador, id=id)
    if request.method == "POST":
        name = jugador.nombre
        jugador.delete()
        messages.success(request, f'Jugador "{name}" eliminado correctamente.')
        return redirect("jugador_list")
    return render(
        request, "registro_futbol/jugador_confirm_delete.html", {"jugador": jugador}
    )
