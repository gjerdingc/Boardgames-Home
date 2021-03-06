from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('players/<int:id>', views.player, name="player"),
    path('new', views.new, name="new"),
    path('gamesplayed', views.gamesplayed, name="gamesplayed"),
    path('players', views.players, name="players"), 
]