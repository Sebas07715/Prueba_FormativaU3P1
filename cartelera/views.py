from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Genero
def inicio(request):
    peliculas = Pelicula.objects.filter(en_cartelera=True).select_related('genero')
    generos = Genero.objects.all()
    q = request.GET.get('q')
    genero_id = request.GET.get('genero')

    if q:
        peliculas = peliculas.filter(titulo__icontains=q)
    
    if genero_id:
        peliculas = peliculas.filter(genero_id=genero_id)
    
    return render(request, 'cartelera/inicio.html', {
    'peliculas': peliculas,
    'generos': generos,
    'q': q or '',
    'genero_sel': int(genero_id) if genero_id else ''
    })

def detalle_pelicula(request, id):
# Retorna 404 si la película no existe o no está en cartelera
    pelicula = get_object_or_404(Pelicula, id=id, en_cartelera=True)
    return render(request, 'cartelera/detalle.html', {'pelicula': pelicula})