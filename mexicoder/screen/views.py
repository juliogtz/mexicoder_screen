from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from .serializers import PlayersSerializer, TeamsSerializer, TrainerSerializer, LeagueSerializer
from .models import Team, League, Player, Trainer

# Create your views here.


class PlayersViewSet(viewsets.ModelViewSet):
    model = Player
    serializer_class = PlayersSerializer
    paginate_by = 1
    filter_fields = ('first_name',)


class TeamsViewSet(viewsets.ModelViewSet):
    model = Team
    serializer_class = TeamsSerializer
    paginate_by = 1
    filter_fields = ('team_name',)


class LeagueViewSet(viewsets.ModelViewSet):
    model = League
    serializer_class = LeagueSerializer
    paginate_by = 1
    filter_fields = ('league_name',)


class TrainerViewSet(viewsets.ModelViewSet):
    model = Trainer
    serializer_class = TrainerSerializer
    paginate_by = 1
    filter_fields = ('first_name',)


@cache_page(60)
def home_view(request):

    return render(request, 'home.html',{

    })

@cache_page(60)
def players_view(request):

    fetch = Player.objects.filter()
    count = fetch.count()
    paginator = Paginator(fetch, 10)
    page = request.GET.get('page')

    try:
        players_list = paginator.page(page)
    except PageNotAnInteger:
        players_list = paginator.page(1)
    except EmptyPage:
        players_list = paginator.page(paginator.num_pages)

    return render(request, 'players.html',{
        'data': players_list
    })


@cache_page(60)
def team_view(request):

    fetch = Team.objects.filter()
    count = fetch.count()
    paginator = Paginator(fetch, 10)
    page = request.GET.get('page')

    try:
        team_list = paginator.page(page)
    except PageNotAnInteger:
        team_list = paginator.page(1)
    except EmptyPage:
        team_list = paginator.page(paginator.num_pages)

    return render(request, 'teams.html',{
        'data': team_list
    })


@cache_page(60)
def trainer_view(request):

    fetch = Trainer.objects.filter()
    count = fetch.count()
    paginator = Paginator(fetch, 10)
    page = request.GET.get('page')

    try:
        trainer_list = paginator.page(page)
    except PageNotAnInteger:
        trainer_list = paginator.page(1)
    except EmptyPage:
        trainer_list = paginator.page(paginator.num_pages)

    return render(request, 'trainers.html',{
        'data': trainer_list
    })


@cache_page(60)
def league_view(request):

    fetch = League.objects.filter()
    count = fetch.count()
    paginator = Paginator(fetch, 10)
    page = request.GET.get('page')

    try:
        league_list = paginator.page(page)
    except PageNotAnInteger:
        league_list = paginator.page(1)
    except EmptyPage:
        league_list = paginator.page(paginator.num_pages)

    return render(request, 'league.html',{
        'data': league_list
    })






