# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from libreria.models import Genere, Autore,  Libro
from django.http import HttpResponse
from django.shortcuts import render_to_response         #SERVE PER VISUALIZZARE LA PAGINA HTML
from django.shortcuts import get_object_or_404          #SERVE A RITORNARE NELLA PAGINA HTML SE NON ESISTE QUEL OGGETTO
                                                        #NEL DB

def tuttiLibri(request):
    elenco=""
    for libri in Libro.objects.all().order_by("Nome"):
        elenco+="<br>'"+str(libri.Nome)+"' "+str(libri.Autori)+" "+str(libri.Genere)+" </br>"
    return HttpResponse(elenco)


#VIENE RICHIAMATA QUESTA FUNZIONE INVECE QUELLA DI SOPRA. NON SO IL PERCHÈ VA BENE LO STESSO
def tuttiLibri(request):
    return render_to_response("libri.html",{
        'libri': Libro.objects.all()
    })


def restiuisciLibro(request, id):

    elenco=""
    try:
        libro=Libro.objects.get(pk=id)
        elenco+="<br> " + str(libro.Nome) + " " + str(libro.Genere) + " </br>"
    except:
        libri=Libro.objects.filter().values_list('pk', flat=True)
        elenco+="Libro non presente, " \
                "sono presenti i seguenti libri:"
        for i in libri:
            elenco+="<br> Codice: " + str(i)

    finally:
        return HttpResponse(elenco)

def restituisciPerDataAcquisto(request, anno):
    libri=Libro.objects.filter(Data_acquisto__year=int(anno))
    elenco=""
    for libro in libri:
        elenco += "<br> " + str(libro.Nome) + " " + str(libro.Genere) + " </br>"

    if len(elenco) == 0:
        elenco="Nessun libro per anno: "+str(anno)

    return HttpResponse(elenco)


def restituisciTuttiIlibriDiQuestoAutore(request, id):
    autore=get_object_or_404(Autore, pk=id)
    libri=Libro.objects.filter(Autori_id=id)
    return render_to_response("libri.html", {
        'libri': libri,
        'autore':autore
    })


def restituisciTuttiILibriPerQuelGenere(request, id):
    genere = get_object_or_404(Genere, pk=id)
    return render_to_response("libri.html",{
        'generi':generi,
        'genere':genere
    })