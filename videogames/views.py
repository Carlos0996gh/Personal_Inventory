from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from .models import Game

from django.core.paginator import Paginator

from .form import GameForm
from django.forms import ModelForm

# Create your views here.

#Pagina principal donde se despliega la colleción de juegos que se tiene.
def index(request):
    #videogame_list = Game.objects.all()`
    videogame_list = Game.objects.raw('SELECT * FROM videogames_game WHERE purchase_status_id = 3 ORDER BY game_purchase_date DESC')

    paginator = Paginator(videogame_list, 15)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {'count' : paginator.count, 'videogame_list' : page}
    return render(request, 'videogames/index.html', context)
    #return HttpResponse("Pagina principal para el inventario de videojuegos")


#Pagina con la forma para insertar nuevos registros.
def add(request):
    form = GameForm
    context = {'form' : form}
    return render(request, 'videogames/add.html', context)

#Inserción de un nuevo videojuego.
def insert(request):
    form = GameForm
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'videogames/add.html', context) 

#Pagina donde se muestra el detalle de algún juego en particular para poder ser editado.
def edit(request, id):
    item = Game.objects.get(pk=id)
    #videogame_list = Game.objects.raw('SELECT * FROM videogames_game WHERE id = %s',[id])
    form = GameForm(instance=item)
    context = {'videogame' : item, 'form' : form}
    return render(request, 'videogames/edit.html', context)

#Actualización a la información de la forma de un videojuego.
def update(request, id):
    item = get_object_or_404(Game, id = id) 
    form = GameForm(request.POST or None, instance=item)
    context = {'videogame' : item, 'form': form}
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'videogames/edit.html', context) 


#Pagina donde se muestra el detalle de algún juego en particular.
def item(request, id):
    item = Game.objects.raw('SELECT * FROM videogames_game WHERE id = %s',[id])
    context = {'videogame' : item}
    return render(request, 'videogames/item.html', context)
