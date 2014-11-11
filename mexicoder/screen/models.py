from django.db import models

# Create your models here

class League(models.Model):
    league_name = models.CharField(max_length=150, blank=True)
    date = models.DateField(blank=True)
    info = models.TextField(blank=True)

class Team(models.Model):
    team_name = models.CharField(max_length=150, blank=True)
    id_league = models.ForeignKey(League)
    date = models.DateField(blank=True)
    info = models.TextField(blank=True)


class Trainer(models.Model):
     first_name = models.CharField(max_length=150, blank=True)
     last_name = models.CharField(max_length=150, blank=True)
     id_team = models.ForeignKey(Team)



class Player(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    common_name = models.CharField(max_length=150, blank=True)
    height = models.CharField(max_length=50, blank=True)
    dob = models.DateField(blank=True)
    foot = models.CharField(max_length=50, blank=True)
    team_id = models.ForeignKey(Team)
    nation_id = models.IntegerField(blank=True)
    attribute1 = models.CharField(max_length=150, blank=True)
    attribute2 = models.CharField(max_length=150, blank=True)
    attribute3 = models.CharField(max_length=150, blank=True)
    attribute4 = models.CharField(max_length=150, blank=True)
    attribute5 = models.CharField(max_length=150, blank=True)
    attribute6 = models.CharField(max_length=150, blank=True)
    rare = models.IntegerField(blank=True)
    rating = models.IntegerField(blank=True)
    type_member = models.CharField(max_length=50, blank=True)
    edition = models.IntegerField(blank=True)

