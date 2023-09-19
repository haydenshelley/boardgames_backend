from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import Boardgame


def index(request):
    boardgames = Boardgame.objects.all().values('name', 'price', 'player')  # or simply .values() to get all fields
    boardgames_list = list(boardgames)  # important: convert the QuerySet to a list object
    return JsonResponse(boardgames_list, safe=False)

def detail(request, boardgame_id):
    return HttpResponse("You're looking at boardgame %s." % boardgame_id)