from django.contrib import admin
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

admin.site.register(Player)
admin.site.register(Amplua)
admin.site.register(Coach)
admin.site.register(Role)
admin.site.register(Season)
admin.site.register(Match)
admin.site.register(Opponent)
admin.site.register(KubanTeam)
admin.site.register(CoachSeason)
admin.site.register(PlayerSeason)