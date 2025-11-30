from gc import get_objects
from django.http import Http404
from django.shortcuts import render
from .models import Tarea

# Lista de objetos Tarea (NO guardados en BBDD)

#lista_tareas = [
#    Tarea(
#        id='01',
#        titulo='Arquitecturas web',
#        descripcion='RA1. Selecciona las arquitecturas y tecnologías de programación Web en entorno servidor, analizando sus capacidades y características propias.',
#        completada=True,
#        fecha_creacion='2025-10-01',
#        fecha_recordatorio='2025-12-09'
#    ),
#    Tarea(
#        id='02',
#        titulo='PHP/Djakarta/Django',
#        descripcion='RA2: Escribe sentencias ejecutables por un servidor Web reconociendo y aplicando procedimientos de integración del código en lenguajes de marcas. RA3. Escribe bloques de sentencias embebidos en lenguajes de marcas, seleccionando y utilizando las estructuras de programación.',
#        completada=True,
#        fecha_creacion='2025-10-14',
#        fecha_recordatorio='2025-12-12'
#    ),
#    Tarea(
#        id='03',
#        titulo='MVC y otros patrones de desarrollo',
#        descripcion='RA5. Desarrolla aplicaciones Web identificando y aplicando mecanismos para separar el código de presentación de la lógica de negocio.',
#        completada=False,
#        fecha_creacion='2025-11-27',
#        fecha_recordatorio='2025-12-14'
#    )
#]

# Create your views here.
def detalle_tarea_view(request, tarea_id):
    # Buscar la tarea por id
    try:
        tarea = Tarea.objects.get(id=tarea_id)
    except Tarea.DoesNotExist:
        raise Http404('Tarea no encontrada')
    # 3 argumentos render(request, template_name, context)
    # Objeto que Django pasa a la vista
    # Nombre de la template
    # Diccionario ({clave:valor})
    return render(request, 'detalle_tarea.html', {'tarea': tarea})
