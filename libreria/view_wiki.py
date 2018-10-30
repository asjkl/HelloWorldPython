import urllib3                                      #LIBRERIA CHE PERMETTE DI FARE RICHIESTA AD UN WEB SERVER
from libreria.models import Autore, Libro, Genere
from django import forms
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from django.http import  JsonResponse               #JSON :)

class WikiRicerca(forms.Form):
    autore=forms.IntegerField(widget=forms.Select(
        choices=[(autore.pk, autore) for autore in Autore.objects.all()]
    ))

    


