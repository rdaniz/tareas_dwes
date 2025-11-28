from django.db import models

# Create your models here.

class Tarea(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now=True)
    fecha_recordatorio = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.titulo}"