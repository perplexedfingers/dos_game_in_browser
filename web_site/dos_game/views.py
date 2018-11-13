from django.http import HttpResponse


def index(request):
    return HttpResponse('index')


def game(request, game_id):
    return HttpResponse('querying %(id)d' % {'id': game_id})
