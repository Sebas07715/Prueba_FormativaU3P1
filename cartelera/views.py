from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Genero, Ticket
from django.shortcuts import redirect
from .forms import TicketForm

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
    pelicula = get_object_or_404(Pelicula, id=id, en_cartelera=True)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.pelicula = pelicula
            ticket.save()
            return redirect('cartelera:ver_ticket', codigo=ticket.codigo)
    else:
        form = TicketForm()
    return render(request, 'cartelera/detalle.html', {'pelicula': pelicula, 'form': form})


def ver_ticket(request, codigo):
    ticket = get_object_or_404(Ticket.objects.select_related('pelicula'), codigo=codigo)
    total_clp = f"${ticket.total():,.0f}".replace(",", ".")
    return render(request, 'cartelera/ticket.html', {'ticket': ticket, 'total_clp': total_clp})