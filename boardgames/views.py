from django.http import HttpResponse
from .models import Boardgame


def index(request):
    latest_question_list = Boardgame.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.name for q in latest_question_list])
    return HttpResponse(output)

def detail(request, boardgame_id):
    return HttpResponse("You're looking at boardgame %s." % boardgame_id)