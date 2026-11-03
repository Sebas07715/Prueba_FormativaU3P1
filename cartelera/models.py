
# Create your models here.
from django.db import models
import uuid

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name="peliculas")
    titulo = models.CharField(max_length=150)
    duracion_min = models.PositiveIntegerField(help_text="Duración en minutos")
    sinopsis = models.TextField()
    afiche = models.ImageField(upload_to='afiches/', blank=True, null=True)
    precio = models.PositiveIntegerField(help_text="Precio en pesos chilenos")
    en_cartelera = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Ticket(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name="tickets")
    nombre_comprador = models.CharField(max_length=100)
    email_comprador = models.EmailField()
    cantidad = models.PositiveIntegerField()
    codigo = models.CharField(max_length=10, unique=True, editable=False)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    def total(self):
        return self.cantidad * self.pelicula.precio

    def __str__(self):
        return f"Ticket {self.codigo} - {self.pelicula.titulo}"