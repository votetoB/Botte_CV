from django.shortcuts import render, Http404, get_object_or_404
from models import Tournament
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournament/home.html', {'tournaments': tournaments})


def index(request, pk):
    the_tournament = get_object_or_404(Tournament, id=pk)
    return render(request, 'tournament/index.html', {'tournament': the_tournament})


def bracket(request, pk):
    raise NotImplementedError