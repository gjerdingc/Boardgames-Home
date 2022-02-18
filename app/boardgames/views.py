from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelform_factory
from boardgames.models import Boardgame, Game, Player
from django.shortcuts import redirect, render, get_object_or_404


def detail(request, id):
    boardgame = AddImageName(Boardgame.objects.get(pk=id))
    return render(request, "boardgames/detail.html", {"boardgame": boardgame})


GameForm = modelform_factory(Game, exclude=[])

def new(request):
    if request.method == "POST":
        # form has been submitted, process data
        form = GameForm(request.POST)
        if form.is_valid():
            form.save() # Creates a meeting instance and saves it into the database
            return redirect("welcome")
    else:   
        form = GameForm()
    return render(request, "boardgames/new.html", {"form": form})

def player(request, id):
    person = Player.objects.get(pk=id)
    game = Game.objects.all()

    queryset = Game.objects.filter(players__name = person).count()

    return render(request, "boardgames/player.html", {
        "game": game, "person": person, "count": queryset
        })

def gamesplayed(request):
    
    return render(request, "boardgames/gamesplayed.html", {
        "games": Game.objects.all(), 
        })

def players(request):

    players_list = []

    for player in Player.objects.all():
        times_played = Game.objects.filter(players__name = player).count()
        player.times_played = times_played
        players_list.append(player)
    
    return render(request, "boardgames/players.html", {
        "players": players_list, 
        })




## Functions

def AddImageName(boardgame):
    boardgame.image_name = boardgame.name.replace(':', '').replace(' ', '-')
    
    return boardgame