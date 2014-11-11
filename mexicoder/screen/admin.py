from django.contrib import admin

# Register your models here.

from .models import Team, League, Player, Trainer

class PlayersAdmin(admin.ModelAdmin):
    search_fields = ('first_name',)

admin.site.register(Player, PlayersAdmin)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Trainer)
