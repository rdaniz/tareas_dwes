# from .views import detalle_tarea_view
from django.urls import path

from tareas.views import DetalleTareaView

# El prefijo 'tareas/' viene del include() en el proyecto.
# Lo que ponga en tareas/urls.py se añade después, en este caso 'tarea/<str:tarea_id>/'.
# Quedará así: http://127.0.0.1:8000/tareas/tarea/id(id asociado a la tarea)/

urlpatterns = [

#    path('tarea/<str:tarea_id>', detalle_tarea_view, name='detalle_tarea'),
    path('tarea/<uuid:pk>/', DetalleTareaView.as_view(), name='detalle_tarea'),
]