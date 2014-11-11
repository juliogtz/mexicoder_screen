from rest_framework import serializers
from .models import Team, League, Player, Trainer

class PlayersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Player
        fields = ('first_name','last_name',)


class TeamsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Team
        fields = ('team_name',)


class LeagueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = League
        fields = ('league_name',)


class TrainerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Trainer
        fields = ('first_name','last_name',)