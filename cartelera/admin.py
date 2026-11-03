from django.contrib import admin
from .models import Genero, Pelicula, Ticket

# Register your models here.

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'precio_chileno', 'en_cartelera')
    list_filter = ('genero', 'en_cartelera',)
    search_fields = ('titulo',)


    @admin.display(description='Precio')

    def precio_chileno(self, obj):
        return f"${obj.precio:,.0f}".replace(",", ".")

@admin.register(Ticket)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'pelicula', 'nombre_comprador', 'cantidad', 'fecha_compra')
    list_filter = ('pelicula',)
    readonly_fields = ('codigo', 'fecha_compra',)

