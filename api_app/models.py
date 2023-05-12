from django.db import models

# Create your models here.
class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_surname = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100)
    player_patronymic = models.CharField(max_length=100, null=True)
    amplua_player = models.ForeignKey('Amplua', on_delete=models.PROTECT)
    player_number = models.CharField(max_length=100)
    player_birthdate = models.DateField()
    player_height = models.CharField(max_length=100)
    player_image = models.CharField(max_length=100, null=True)

class Amplua(models.Model):
    amplua_id = models.AutoField(primary_key=True)
    amplua_name = models.CharField(max_length=100)

class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)
    coach_surname = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    coach_patronymic = models.CharField(max_length=100, null=True)
    coach_info = models.CharField(max_length=100)
    coach_birthdate = models.DateField()
    role_coach = models.ForeignKey('Role', on_delete=models.PROTECT)
    coach_image = models.CharField(max_length=100, null=True)

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)

class Season(models.Model):
    season_id = models.AutoField(primary_key=True)
    season_name = models.CharField(max_length=100)
    season_start = models.DateField()
    season_end = models.DateField()

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    match_scoreopponent = models.PositiveIntegerField()
    match_scorekuban = models.PositiveIntegerField()
    match_date = models.DateField()
    match_opponent = models.ForeignKey('Opponent', on_delete=models.PROTECT)
    match_kuban = models.ForeignKey('KubanTeam', on_delete=models.PROTECT)

class Opponent(models.Model):
    opponent_id = models.AutoField(primary_key=True)
    opponent_name = models.CharField(max_length=100)
    opponent_image = models.CharField(max_length=100, null=True)

class KubanTeam(models.Model):
    kubanteam_id = models.AutoField(primary_key=True)
    kubanteam_image = models.CharField(max_length=100, null=True)
    kubanteam_name = models.CharField(max_length=100)

class CoachSeason(models.Model):
    coachseason_id = models.AutoField(primary_key=True)
    coachseason_coachid = models.ForeignKey('Coach', on_delete=models.PROTECT)
    coachseason_seasonid = models.ForeignKey('Season', on_delete=models.PROTECT)

class PlayerSeason(models.Model):
    playerseason_id = models.AutoField(primary_key=True)
    playerseason_playerid = models.ForeignKey('Player', on_delete=models.PROTECT)
    playerseason_seasonid = models.ForeignKey('Season', on_delete=models.PROTECT)


