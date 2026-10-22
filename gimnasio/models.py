from django.db import models
from django.db.models import Count, F
from django.utils import timezone


class Disciplina(models.Model):
    nombre = models.CharField(max_length=40)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Socio(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=120)
    correo = models.EmailField()
    vence_membresia = models.DateField()

    class Meta:
        ordering = ["numero"]

    def __str__(self):
        return f"{self.numero} {self.nombre}"

    @property
    def membresia_vigente(self):
        return self.vence_membresia >= timezone.localdate()


class ClaseQuerySet(models.QuerySet):
    def con_lugar(self):
        """Clases en las que todavía se puede inscribir alguien."""
        return self.annotate(num_inscritos=Count("inscritos")).filter(
            num_inscritos__lte=F("cupo")
        )


class Clase(models.Model):
    class Dia(models.TextChoices):
        LUNES = "lun", "Lunes"
        MARTES = "mar", "Martes"
        MIERCOLES = "mie", "Miércoles"
        JUEVES = "jue", "Jueves"
        VIERNES = "vie", "Viernes"
        SABADO = "sab", "Sábado"

    class Estado(models.TextChoices):
        ACTIVA = "activa", "Activa"
        CANCELADA = "cancelada", "Cancelada"

    codigo = models.CharField(max_length=10, unique=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name="clases")
    instructor = models.CharField(max_length=80)
    dia = models.CharField(max_length=3, choices=Dia.choices)
    hora = models.TimeField()
    cupo = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.ACTIVA)
    sala = models.CharField(max_length=30, blank=True)
    inscritos = models.ManyToManyField(Socio, related_name="clases", blank=True)

    objects = ClaseQuerySet.as_manager()

    class Meta:
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} {self.disciplina} {self.get_dia_display()} {self.hora:%H:%M}"
