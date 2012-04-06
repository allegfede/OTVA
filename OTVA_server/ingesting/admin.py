from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from OTVA_server.ingesting.models import *
from OTVA_server.ingesting.forms import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')

class EpisodeOption(admin.ModelAdmin):
    list_display = ('program', 'episode_number', 'name', 'lenght', 'created')

class FasciapubblicitariaOption(admin.ModelAdmin):
    list_display = ('canale', 'orario_previsto', 'get_validita_settimanale')
    form = FasciapubblicitariaForm

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Week)
admin.site.register(Playback)
admin.site.register(Channel)
admin.site.register(Program)
admin.site.register(Episode, EpisodeOption)
admin.site.register(Agente)
admin.site.register(Cliente)
admin.site.register(Fasciapubblicitaria, FasciapubblicitariaOption)
