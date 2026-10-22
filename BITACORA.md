# Bitácora del examen

**Nombre:**
**Repositorio:**

Copia el bloque de abajo una vez por cada falla que encuentres. Llénalo en el momento, no al final.

---

## Falla: Parte 1

Parte 1: python manage.py migrate
**Síntoma:** RuntimeError: Model class gimnasio.models.Disciplina doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.

**Causa raíz:** la aplcación de 'gimnasio' (la carpeta) no estaba declarada dentro de installed apps en settings.

**Corrección:** en settings.py, agregue 'gimnasio'

**Verificación:** me permitió hacer las migraciones

Parte 2: python manage.py cargar_datos
**Síntoma:** 
1. django.db.utils.OperationalError: no such column: gimnasio_clase.sala
2. django.db.utils.IntegrityError: UNIQUE constraint failed: gimnasio_disciplina.nombre

**Causa raíz:**
1. las migraciones para agregar la sala al modelo no estaban aplicadas.
2. el nombre de la disciplina estaba marcado como unique, al revisar el json, me di cuenta que se repiten. por lo tanto, no puede ser único.

**Corrección:** 
1. hice 'makemigrations' (y mostró que se había aregado salas), se agregó la migración 002.
2. borré el unique en nombre de disciplina, hice las migraciones y se agregó la migración 003.

**Verificación:** 
1. ya aparecía 'sala' en las migraciones y me salió otro error (el de nombre disciplina).
2. apareció el 'carga terminada' :) y el número de los contadores. 
Socios: 40
Clases: 20

**Commit:** parte 1: migración inicial, aregar 'salas' al modelo, agrear 'gimnasio' a installed apps y modificar el modelo de disciplinas.

## Falla: Ticket 1
**Síntoma:** django.urls.exceptions.NoReverseMatch: Reverse for 'detalle_clase' not found. 'detalle_clase' is not a valid view function or pattern name.

**Causa raíz:** en 'clase_lista' el url de 'clase_detalle' estaba mal escrito.

**Corrección:** escribir el nombre correcto del archivo 'clase_detalle.html' en el archivo de clase lista

**Corrección:** la página cargó correctamente

**Commit:** ticket 1: corregir el nombre de 'clase_detalle' en 'clase_lista'

## Falla: Ticket 2
**Síntoma:** La página principal dice que hay 20 clases con lugares disponibles, y no puede ser

**Causa raíz:** no tomabamos en cuenta el estado de la clase

**Corrección:** agregarlo al filtro de queryset en models

**Commit:** ticket 2: agregar el estado de la clase al queryset.

## Falla: Ticket 3
**Síntoma:** En el buscador (`/clases/buscar/`) escribo 'yoga' y salen 39 resultados. Solo tenemos 4 clases de yoga

**Causa raíz:** en views, no teníamos el distinct en la parte de búsqueda.

**Corrección:** agregar .distinct() a la búsqueda

**Verificación:** Salen los resultados correctos.

**Commit:** ticket 3: agregar distinct() a la búsqueda en views.

---

## Declaración de uso de IA

Marca una opción.

- [x] No usé asistentes de IA en este examen.
- [ ] Sí usé asistentes de IA. Para cada uso: herramienta, qué le pedí, qué usé de su respuesta y qué revisé o cambié yo.

consulté la documentación de SQLite para la parte 1. Específicamente para la parte de unique :) https://www.sqlite.org/search?s=d&q=integrity+error