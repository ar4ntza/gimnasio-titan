from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render

from .models import Clase


def clase_lista(request):
    solo_con_lugar = request.GET.get("con_lugar") == "1"
    if solo_con_lugar:
        clases = Clase.objects.con_lugar()
    else:
        clases = Clase.objects.annotate(num_inscritos=Count("inscritos"))
    contexto = {
        "clases": clases.select_related("disciplina"),
        "solo_con_lugar": solo_con_lugar,
        "total_con_lugar": Clase.objects.con_lugar().count(),
    }
    return render(request, "gimnasio/clase_lista.html", contexto)


def clase_detalle(request, pk):
    clase = get_object_or_404(Clase.objects.select_related("disciplina"), pk=pk)
    contexto = {"clase": clase, "inscritos": clase.inscritos.all()}
    return render(request, "gimnasio/clase_detalle.html", contexto)


def clase_buscar(request):
    q = request.GET.get("q", "").strip()
    clases = Clase.objects.none()
    if q:
        clases = Clase.objects.filter(
            Q(disciplina__nombre__icontains=q)
            | Q(instructor__icontains=q)
            | Q(inscritos__nombre__icontains=q)
        ).select_related("disciplina").distinct()
    contexto = {"q": q, "clases": clases}
    return render(request, "gimnasio/clase_buscar.html", contexto)
