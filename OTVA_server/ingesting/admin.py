from django.contrib import admin

from OTVA_server.ingesting.models import Playback, Channel, Program, Episode
class EpisodeOption(admin.ModelAdmin):
    list_display = ('program', 'episode_number', 'name', 'lenght', 'created')

admin.site.register(Playback)
admin.site.register(Channel)
admin.site.register(Program)
admin.site.register(Episode, EpisodeOption)
