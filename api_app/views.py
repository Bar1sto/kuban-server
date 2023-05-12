from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import Player
from .models import Amplua
from .models import Coach
from .models import Role
from .models import Season
from .models import Match
from .models import Opponent
from .models import KubanTeam
from .models import CoachSeason
from .models import PlayerSeason
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
@method_decorator(csrf_exempt, name = 'dispatch')

class PlayerList(View):
    def post(self, request):
        data = json.load(request.body.decode("utf-8"))
        p_surname = data.get('player_surname')
        p_name = data.get('player_name')
        p_patronymic = data.get('player_patronymic')
        p_ampluaName = data.get('amplua_player')
        p_number = data.get('player_number')
        p_birthdate = data.get('player_birthdate')
        p_image = data.get('player_image')

        player_data = {
            'player_surname': p_surname,
            'player_name': p_name,
            'player_patronymic': p_patronymic,
            'amplua_player': p_ampluaName,
            'player_number': p_number,
            'player_birthdate': p_birthdate,
            'player_image': p_image,
        }

        player = Player.objects.create(**player_data)

        data = {
            "message": f"New player added to table Players with id: {player.id}"
        }




        return JsonResponse(data, status=201)

    def get(self, request):
        player_count = Player.objects.count()
        player_all = Player.objects.all()

        player_data = []
        for player in player_all:
            player_data.append({
                'player_surname': player.player_surname,
                'player_name': player.player_name,
                'player_patronymic': player.player_patronymic,
                'player_number': player.player_number,
                'player_birthdate': player.player_birthdate,
                'player_image': player.player_image,
                'amplua_player': player.amplua_player.amplua_name,
            })
        data = {
            'player_items': player_data,
            'player_count': player_count,
        }

        return JsonResponse(data)

class AmpluaList(View):
    def post(self, request):
        data_amplua = json.load(request.body.decode("utf-8"))
        p_ampluaname = data_amplua.get('amplua_name')

        amplua_data = {
            'amplua_name': p_ampluaname,
        }

        amplua = Amplua.objects.create(**amplua_data)

        data_amplua = {
            "message": f"Новая амплуа добавлена успешно! Индификатор автоматический: {amplua.id}"
        }
        return JsonResponse(data_amplua, status=201)

    def get(self, request):
        amplua_count = Amplua.objects.count()
        amplua_all = Amplua.objects.all()

        amplua_data = []
        for amplua in amplua_all:
            amplua_data.append({
                'amplua_name': amplua.amplua_name,
            })

        data = {
            'amplua_items': amplua_data,
            'amplua_count': amplua_count,
        }
        return JsonResponse(data)

class CoachList(View):
    def post(self, request):
        data_coach = json.load(request.body.decode("utf-8"))
        p_coachsurname = data_coach.get('coach_surname')
        p_coachname = data_coach.het('coach_name')
        p_coachpatronymic = data_coach.get('coach_patronymic')
        p_coachinfo = data_coach.get('coach_info')
        p_coachbirthdate = data_coach.get('coach_birthdate')
        p_coachrole = data_coach.get('role_coach')
        p_coachimage = data_coach.get('coach_image')

        coach_data = {
            'coach_surname': p_coachsurname,
            'coach_name': p_coachname,
            'coach_patronymic': p_coachpatronymic,
            'coach_info': p_coachinfo,
            'coach_birthdate': p_coachbirthdate,
            'role_coach': p_coachrole,
            'coach_image': p_coachimage,
        }

        coach = Coach.objects.create(**coach_data)

        data_coach = {
            "message": f"Новый тренер  добавлена успешно! Индификатор автоматический: {coach.id}"
        }
        return JsonResponse(data_coach, status=201)

    def get(self, request):
        coach_count = Coach.objects.count()
        coach_all = Coach.objects.all()

        coach_data = []
        for coach in coach_all:
            coach_data.append({
                'coach_surname':coach.coach_surname,
                'coach_name': coach.coach_name,
                'coach_patronymic': coach.coach_patronymic,
                'coach_info': coach.coach_info,
                'coach_birthdate': coach.coach_birthdate,
                'role_coach': coach.role_coach.role_name,
                'coach_image': coach.coach_image,
            })

        data = {
            'coach_items': coach_data,
            'coach_count': coach_count,
        }
        return JsonResponse(data)

class RoleList(View):
    def post(self, request):
        data_role = json.load(request.body.decode("utf-8"))
        p_rolename = data_role.get('role_name')

        role_data = {
            'role_name': p_rolename
        }

        role = Role.objects.create(**role_data)

        data_role = {
            "message": f"Новая роль добавлена успешно! Индификатор автоматический: {role.id}"
        }
        return JsonResponse(data_role, status=201)

    def get(self, request):
        role_count = Role.objects.count()
        role_all = Role.objects.all()

        role_data = []
        for role in role_all:
            role_data.append({
                'role_name': role.role_name,
            })

        data = {
            'role_items': role_data,
            'role_count': role_count,
        }
        return JsonResponse(data)

class SeasonList(View):
    def post(self, request):
        data_season = json.load(request.body.decode("utf-8"))
        p_seasonname = data_season.get('season_name')
        p_seasonstart = data_season.get('season_start')
        p_seasonend = data_season.get('season_end')

        season_data = {
            'season_name': p_seasonname,
            'season_start': p_seasonstart,
            'season_end': p_seasonend,
        }

        season = Season.objects.create(**season_data)

        data_season = {
            "message": f"Новый сезон добавлена успешно! Индификатор автоматический: {season.id}"
        }
        return JsonResponse(data_season, status=201)
    def get(self, request):
        season_count = Season.objects.count()
        season_all = Season.objects.all()

        season_data = []
        for season in season_all:
            season_data.append({
                'season_name': season.season_name,
                'season_start': season.season_start,
                'season_end': season.season_end,
            })
        data = {
            'season_items': season_data,
            'season_count': season_count,
        }
        return JsonResponse(data)

class MatchList(View):
    def post(self, request):
        data_match = json.load(request.body.decode("utf-8"))
        p_matchscoreopponent = data_match.get('match_scoreopponent')
        p_matchscorekuban = data_match.get('match_scorekuban')
        p_matchdate = data_match.get('match_date')
        p_matchopponent = data_match.get('match_opponent')
        p_matchkuban = data_match.get('match_kuban')

        match_data = {
            'match_scoreopponent': p_matchscoreopponent,
            'match_scorekuban': p_matchscorekuban,
            'match_date': p_matchdate,
            'match_opponent': p_matchopponent,
            'match_kuban': p_matchkuban,
        }

        match = Match.objects.create(**match_data)

        data_match = {
            "message": f"Новый матч добавлена успешно! Индификатор автоматический: {match.id}"
        }
        return JsonResponse(data_match, status=201)
    def get(self, request):
        match_count = Match.objects.count()
        match_all = Match.objects.all()

        match_data = []
        for match in match_all:
            match_data.append({
                'match_scoreopponent': match.match_scoreopponent,
                'match_scorekuban': match.match_scorekuban,
                'match_date': match.match_date,
                'match_opponent': match.match_opponent,
                'match_kuban': match.match_kuban,
            })
        data = {
            'match_items': match_data,
            'match_count': match_count,
        }
        return JsonResponse(data)

class OpponentList(View):
    def post(self, request):
        data_opponent = json.load(request.body.decode("utf-8"))
        p_opponentname = data_opponent.get('opponent_name')
        p_opponentimage = data_opponent.get('opponent_image')

        opponent_data = {
            'opponent_name': p_opponentname,
            'opponent_image': p_opponentimage,
        }

        opponent = Opponent.objects.create(**opponent_data)

        data_opponent = {
            "message": f"Новый соперник добавлена успешно! Индификатор автоматический: {opponent.id}"
        }
        return JsonResponse(data_opponent, status=201)
    def get(self, request):
        opponent_count = Opponent.objects.count()
        opponent_all = Opponent.objects.all()

        opponent_data = []
        for opponent in opponent_all:
            opponent_data.append({
                'opponent_name': opponent.opponent_name,
                'opponent_image': opponent.opponent_image,
            })
        data = {
            'opponent_items': opponent_data,
            'opponent_count': opponent_count,
        }
        return JsonResponse(data)

class KubanTeamList(View):
    def post(self, request):
        data_kubanteam = json.load(request.body.decode("utf-8"))
        p_kubanteamname = data_kubanteam.get('kubanteam_name')
        p_kubanteamimage = data_kubanteam.get('kubanteam_image')

        kubanteam_data = {
            'kubanteam_name': p_kubanteamname,
            'kubanteam_image': p_kubanteamimage,
        }

        kubanteam = KubanTeam.objects.create(**kubanteam_data)

        data_kubanteam = {
            "message": f"Новая команда добавлена успешно! Индификатор автоматический: {kubanteam.id}"
        }
        return JsonResponse(data_kubanteam, status=201)
    def get(self, request):
        kubanteam_count = KubanTeam.objects.count()
        kubanteam_all = KubanTeam.objects.all()

        kubanteam_data = []
        for kubanteam in kubanteam_all:
            kubanteam_data.append({
                'kubanteam_name': kubanteam.kubanteam_name,
                'kubanteam_image': kubanteam.kubanteam_image,
            })
        data = {
            'kubanteam_items': kubanteam_data,
            'kubanteam_count': kubanteam_count,
        }
        return JsonResponse(data)

class CoachSeasonList(View):
    def post(self, request):
        data_coachseason = json.load(request.body.decode("utf-8"))
        p_coachseasoncoach = data_coachseason.get('coachseason_coachid')
        p_coachseasonseason = data_coachseason.get('coachseason_seasonid')

        coachseason_data = {
            'coachseason_coachid': p_coachseasoncoach,
            'coachseason_seasonid': p_coachseasonseason,
        }
        coachseason = CoachSeason.objects.count(**coachseason_data)

        data_coachseason = {
            "message": f"Новая информация добавлена успешно! Индификатор автоматический: {coachseason.id}"
        }
        return JsonResponse(data_coachseason, status=201)
    def get(self, request):
        coachseason_count = CoachSeason.objects.count()
        coachseason_all = CoachSeason.objects.all()

        coachseason_data = []
        for coachseason in coachseason_all:
            coachseason_data.append({
                'coachseason_coachid': coachseason.coachseason_coachid.coach_id,
                'coachseason_seasonid': coachseason.coachseason_seasonid.season_id,
            })
        data = {
            'coachseason_items': coachseason_data,
            'coachseason_count': coachseason_count,
        }
        return JsonResponse(data)

class PlayerSeasonList(View):
    def post(self, request):
        data_playerseason = json.load(request.body.decode("utf-8"))
        p_playerseasonplayer = data_playerseason.get('playerseason_playerid')
        p_playerseasonseason = data_playerseason.het('playerseason_seasonid')

        playerseason_data = {
            'playerseason_playerid': p_playerseasonplayer,
            'playerseason_seasonid': p_playerseasonseason,
        }
        playerseason = PlayerSeason.objects.count(**playerseason_data)

        data_playerseason = {
            "message": f"Новая информация добавлена успешно! Индификатор автоматический: {playerseason.id}"
        }
        return JsonResponse(data_playerseason, status=201)
    def get(self, request):
        playerseason_count = PlayerSeason.objects.count()
        playerseason_all = PlayerSeason.objects.all()

        playerseason_data = []
        for playerseason in playerseason_all:
            playerseason_data.append({
                'playerseason_playerid': playerseason.playerseason_playerid.player_id,
                'playerseason_seasonid': playerseason.playerseason_seasonid.season_id,
            })
        data = {
            'playerseason_items': playerseason_data,
            'playerseason_count': playerseason_count,
        }
        return JsonResponse(data)



