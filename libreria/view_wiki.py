import urllib2  # LIBRERIA CHE PERMETTE DI FARE RICHIESTA AD UN WEB SERVER
from libreria.models import Autore, Libro, Genere
from django import forms
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from json import JSONDecoder  # JSON :)
from django.views.decorators.csrf import csrf_exempt

wiki_url_api = "https://%s.wikipedia.org/w/api.php?action=query&format=json&srlimit=%s&list=search&srsearch=%s"
wiki_link = "https://%s.wikipedia.org/wiki/"

dizionarioLingua = {0: "it",
                    1: "en"}


class WikiRicerca(forms.Form):
    autore = forms.IntegerField(widget=forms.Select(
        choices=[(autore.pk, autore) for autore in Autore.objects.all()]
    ))

    wikipedia = forms.IntegerField(widget=forms.RadioSelect(
        choices=((0, "Italiano"), (1, "Inglese"))
    ))

    limite = forms.IntegerField(initial=10, widget=forms.RadioSelect(
        choices=((10, "10"), (50, "50"), (100, "100"))
    ))

    def clean_limite(self):
        if (self.cleaned_data['limite'] > 50 and self.cleaned_data['wikipedia'] == 1):
            raise forms.ValidationError("Massimo 50 risultati in Inglese")
        return self.cleaned_data['limite']


@csrf_exempt
def ricerca(request):
    risultati = link = None
    if request.method == 'POST':
        form = WikiRicerca(request.POST)
        if form.is_valid():
            autoreDaCercare = Autore.objects.get(pk=form.cleaned_data['autore'])
            url = wiki_url_api % (dizionarioLingua.get(form.cleaned_data['wikipedia']), form.cleaned_data['limite'],
                                  str(autoreDaCercare).replace(" ", "%"))
            link = wiki_link % dizionarioLingua.get(form.cleaned_data['wikipedia'])
            dati = urllib2.urlopen(url.encode('utf-8')).read()
            valori = JSONDecoder().decode(dati)
            risultati = valori['query']['search']

    else:
        form = WikiRicerca()

    return render_to_response('ricercaWiki.html', {
        'form': form,
        'link': link,
        'risultati': risultati,
    })
