from django.http import HttpResponse
from django.template import loader
from .models import Boardgame


def index(request):
    latest_boardgame_list = Boardgame.objects.order_by("id")[:5]
    template = loader.get_template("boardgames/index.html")
    context = {
        "latest_boardgame_list": latest_boardgame_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, boardgame_id):
    return HttpResponse("You're looking at boardgame %s." % boardgame_id)