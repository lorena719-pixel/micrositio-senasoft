from django.shortcuts import redirect, render

from .models import Competidor


def inicio(request):
    return render(request, "competidores/inicio.html")


def registro(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        centro = request.POST.get("centro", "").strip()
        categoria = request.POST.get("categoria", "").strip()

        if nombre and centro and categoria:
            Competidor.objects.create(
                nombre=nombre,
                centro=centro,
                categoria=categoria,
            )
            return redirect("lista_competidores")

    return render(request, "competidores/registro.html")


def lista_competidores(request):
    competidores = Competidor.objects.all()
    return render(
        request,
        "competidores/competidores.html",
        {"competidores": competidores},
    )