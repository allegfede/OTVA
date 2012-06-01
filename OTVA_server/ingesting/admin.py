from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from OTVA_server.ingesting.models import *
from OTVA_server.ingesting.forms import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    search_fields = ('first_name', 'last_name')
    
class ChannelOption(admin.ModelAdmin):
    list_display = ('name', 'tv_number', 'logo_img')
    search_fields = ('name',)
    
class ProgramOption(admin.ModelAdmin):
    list_display = ('name', 'season', 'tags', 'promo_folder', 'default_lenght', 'replicabile', 'formato', 'classificazione_registro')
    search_fields = ('name',)
    list_filter = ('default_lenght', 'replicabile', 'formato')

class EpisodeOption(admin.ModelAdmin):
    list_display = ('program', 'episode_number', 'name', 'lenght', 'created')
    search_fields = ('name',)
    list_filter = ('program',)
    
class AgenteOption(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'citta', 'cellulare', 'telefono', 'email')
    list_filter = ('citta',)
    search_fields = ('nome', 'cognome')

class ClienteOption(admin.ModelAdmin):
    list_display = ('ragione_sociale', 'codife_fiscale', 'partita_iva', 'citta', 'provincia', 'contatto_commerciale', 'agente', 'telefono', 'cellulare', 'email')
    search_fields = ('ragione_sociale', 'codife_fiscale', 'partita_iva',)
    list_filter = ('citta', 'provincia')

class FasciapubblicitariaOption(admin.ModelAdmin):
    list_display = ('canale', 'orario_previsto', 'validita_settimanale')
    form = FasciapubblicitariaForm
    list_filter = ('canale', 'validitasettimanale')
    
class ContrattoOption(admin.ModelAdmin):
    list_display = ('codice_contratto', 'cliente', 'agente', 'data', 'servizi_richiesti')
    search_fields = ('codice_contratto', 'cliente')

class PlaylistOption(admin.ModelAdmin):
    list_display = ('name','date','start','programma',)
    form = PlaylistForm
    #search_fields = ('programmi',)
    list_filter = ('date','start',)

class PlaybackOption(admin.ModelAdmin):
    list_display = ('channel', 'current_state', 'playlists', 'server_ip', 'server_port')
    form = PlaybackForm
    search_fields = ('channel',)
    list_filter = ('current_state', 'server_ip',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Week)
admin.site.register(Channel, ChannelOption)
admin.site.register(Program, ProgramOption)
admin.site.register(Episode, EpisodeOption)
admin.site.register(Agente, AgenteOption)
admin.site.register(Cliente, ClienteOption)
admin.site.register(Fasciapubblicitaria, FasciapubblicitariaOption)
admin.site.register(Contratto, ContrattoOption)
admin.site.register(Playback, PlaybackOption)
admin.site.register(Playlist, PlaylistOption)