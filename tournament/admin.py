from django.contrib import admin
from tournament.models import Tournament, Match, Registration


class TournamentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Registration)
admin.site.register(Match)