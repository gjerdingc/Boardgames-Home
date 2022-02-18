from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from boardgames.models import Game, Boardgame, Player


def welcome(request):

    boardgames_list = []
    players_list = []

    ## Add counts of times played based on data from games table
    for boardgame in Boardgame.objects.all():
        boardgame = AddImageName(boardgame)
        times_played = Game.objects.filter(boardgame__name = boardgame.name).count()
        boardgame.times_played = times_played
        boardgames_list.append(boardgame)
    
    for player in Player.objects.all():
        times_played = Game.objects.filter(players__name = player).count()
        player.times_played = times_played
        players_list.append(player)

    
    return render(request, "website/welcome.html", {
        "boardgames": boardgames_list, 
        "games": Game.objects.all(), 
        "players": players_list,
        })

    

## Functions

def AddImageName(boardgame):
    boardgame.image_name = boardgame.name.replace(':', '').replace(' ', '-')
    boardgame.image_name = '/static/boardgames/' + boardgame.image_name + '.jpg'
    
    return boardgame