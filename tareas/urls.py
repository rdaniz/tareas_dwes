from .views import detalle_tarea_view
from django.urls import path

# El prefijo 'tareas/' viene del include() en el proyecto.
# Lo que ponga en tareas/urls.py se añade después, en este caso 'tarea/<str:tarea_id>/'.
# Quedará así: http://127.0.0.1:8000/tareas/tarea/01/

urlpatterns = [
    path('tarea/<str:tarea_id>', detalle_tarea_view, name='detalle_tarea'),
]