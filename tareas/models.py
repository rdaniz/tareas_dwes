import uuid
from django.db import models

# Create your models here.

class Tarea(models.Model):
    # Añado default=uuid.uuid4 e import.uuid para que se generen automáticamente los id
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_recordatorio = models.DateTimeField(auto_now=False, auto_now_add=False)

    # Además del título muestro el id para poder añadirlo a la url y buscar la tarea
    def __str__(self):
        return f"{self.titulo} - {self.id}"