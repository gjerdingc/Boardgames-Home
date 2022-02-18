from django.contrib import admin

from boardgames.models import Boardgame, Player, Game, Score, Rating

admin.site.register(Boardgame)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Score)
admin.site.register(Rating)