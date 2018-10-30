import urllib2  # LIBRERIA CHE PERMETTE DI FARE RICHIESTA AD UN WEB SERVER
from libreria.models import Autore, Libro, Genere
from django import forms
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from json import JSONDecoder  # JSON :)
from django.views.decorators.csrf import csrf_exempt



wiki_url_api = "https://%.wikipedia.org/w/api.php?action=query&format=json&srlimit=%&list=search&srsearch=%"
wiki_link = "https://%.wikipedia.org/wiki/"


class WikiRicerca(forms.Form):
    autore = forms.IntegerField(widget=forms.Select(
        choices=[(autore.pk, autore) for autore in Autore.objects.all()]
    ))

    wikipedia = forms.IntegerField(widget=forms.RadioSelect(
        choices=(("it", "Italiano"), ("en", "Inglese"))
    ))

    limite = forms.IntegerField(initial=10, widget=forms.RadioSelect(
        choices=((10, "10"), (50, "50"), (100, "100"))
    ))

@csrf_exempt
def ricerca(request):
    risultati = link = None
    if request.method == 'POST':
        form = WikiRicerca(request.POST)
        print("ciao11")
        if form.is_valid():
            print("ciao")
            autoreDaCercare = get_object_or_404(Autore, pk=form.cleaned_data['autore'])
            url = wiki_url_api % (form.cleaned_data['wikipedia'], form.cleaned_data['limite'], autoreDaCercare.cognome)
            link = wiki_link % form.cleaned_data['wikipedia']
            dati = urllib2.urlopen(url.encode('utf-8')).read()
            valori = JSONDecoder().decode(dati)
            risultati = valori['query']['search']
            print(url)
    else:
        form = WikiRicerca()

    return render_to_response('ricercaWiki.html', {
        'form': form,
        'link': link,
        'risultati': risultati,
    })
