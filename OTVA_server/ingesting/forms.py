# -*- coding: utf-8 -*-
from django import forms
from OTVA_server.ingesting.models import Week, Fasciapubblicitaria, Playlist
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