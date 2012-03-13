from django.contrib import admin

from OTVA_server.ingesting.models import *
class EpisodeOption(admin.ModelAdmin):
    list_display = ('program', 'serie', 'name', 'lenght', 'created')
admin.site.register(Channel)
admin.site.register(Program)
admin.site.register(Episode, EpisodeOption)
admin.site.register(Playback)