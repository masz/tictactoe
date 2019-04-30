from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from gameplay.models import Game


@login_required
def home(request):
    all_my_games = Game.objects.games_for_user(request.user)
    active_games = all_my_games.active()

    return render(request, "player/home.html", {'games': active_games})

