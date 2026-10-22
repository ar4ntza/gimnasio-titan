# Bitácora del examen

**Nombre:**
**Repositorio:**

Copia el bloque de abajo una vez por cada falla que encuentres. Llénalo en el momento, no al final.

---

## Falla N (Parte 1 / Ticket N / F1 / F2 / Extra)

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

---

## Declaración de uso de IA

Marca una opción.

- [ ] No usé asistentes de IA en este examen.
- [ ] Sí usé asistentes de IA. Para cada uso: herramienta, qué le pedí, qué usé de su respuesta y qué revisé o cambié yo.
