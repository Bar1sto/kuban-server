from django.urls import path
from .views import PlayerList
from .views import AmpluaList
from .views import CoachList
from .views import RoleList
from .views import SeasonList
from .views import MatchList
from .views import OpponentList
from .views import KubanTeamList
from .views import CoachSeasonList
from .views import PlayerSeasonList


urlpatterns = [
    path('player/', PlayerList.as_view()),
    path('amplua/', AmpluaList.as_view()),
    path('coach/', CoachList.as_view()),
    path('role/', RoleList.as_view()),
    path('season/', SeasonList.as_view()),
    path('match/', MatchList.as_view()),
    path('opponent/', OpponentList.as_view()),
    path('kubanteam/', KubanTeamList.as_view()),
    path('coachseason/', CoachSeasonList.as_view()),
    path('playerseason/', PlayerSeasonList.as_view()),

]
