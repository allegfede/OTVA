from django import forms
from OTVA_server.ingesting.models import Fasciapubblicitaria


class FasciapubblicitariaForm(forms.ModelForm):
    class Meta:
        model = Fasciapubblicitaria
