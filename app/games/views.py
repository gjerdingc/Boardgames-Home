from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelform_factory
from boardgames.models import Boardgame, Game
from django.shortcuts import redirect, render, get_object_or_404

def detail(request, id):
    game = Game.objects.get(pk=id)
    return render(request, "games/detail.html", {"game": game})

