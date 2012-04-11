# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms
from OTVA_server.ingesting.models import *
from OTVA_server.ingesting.widgets import *
from django.utils.translation import ugettext_lazy as _


class FasciapubblicitariaForm(forms.ModelForm):
    validitasettimanale = forms.ModelMultipleChoiceField(
        queryset=Week.objects.all(),
        required=True,
        widget=ColumnCheckboxSelectMultiple,
        label='Validita settimanale',
        )
    class Meta:
        model = Fasciapubblicitaria
        
class PlaylistForm(forms.ModelForm):
    programmi = forms.ModelMultipleChoiceField(
        Episode.objects.all(),
        #required=True,
        widget=FilteredSelectMultiple("Programmi",True,attrs={'rows':'100'}),
        )
    class Meta:
        model = Playlist

class PlaybackForm(forms.ModelForm):
    playlist = forms.ModelMultipleChoiceField(
        Playlist.objects.all(),
        #required=True,
        widget=FilteredSelectMultiple("Playlists",True,attrs={'rows':'100'}),
        )
    class Meta:
        model = Playback