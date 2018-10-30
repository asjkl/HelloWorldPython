# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from libreria.models import *

a1 = Autore(Nome="Giovanni", Cognome="Sapia")
a2 = Autore(Nome="Michele", Cognome="Cataldo")
a3 = Autore(Nome="Giuseppe", Cognome="Rossi")

a1.save()
a2.save()
a3.save()

g1 = Genere(Nome="Genere1")
g2 = Genere(Nome="Genere2")
g3 = Genere(Nome="Genere3")
g4 = Genere(Nome="Genere4")
g5 = Genere(Nome="Genere5")

g1.save()
g2.save()
g3.save()
g4.save()
g5.save()

list_id_autori = []
list_id_autori.append(a1.id)
list_id_autori.append(a2.id)
list_id_autori.append(a3.id)

list_id_generi=[]
list_id_generi.append(g1.id)
list_id_generi.append(g2.id)
list_id_generi.append(g3.id)
list_id_generi.append(g4.id)
list_id_generi.append(g5.id)

#for x in list_id_autori:
#    print x

l1 = Libro(Nome="Libro1")
l1.Autori_id=list_id_autori[0]                 #RELAZIONE UNO A MOLTI
l1.Autori_id=list_id_autori[1]
l1.Generi_id=list_id_generi[0]
l1.Generi_id=list_id_generi[1]
l1.save()

#Autore.objects.all()                                                    #RESTITUISCI TUTTI GLI AUTORI
#for a in Autore.object.all().order_by("descrizione")                    #ORDINAMI TUTTI GLI AUTORI PER "descrizione"
#for a in Autore.object.all().filter(cognome__contains="o")              #VISUALIZZA TUTTI I COGNOMI CHE CONTENGONO "o"
#for a in Autore.object.all().filter(autore__cognome="Sapia")            #VISUALIZZA TUTTI GLI AUTORI CHE HANNO COME
#Libro.objects.filter().values_list('pk', flat=True)                     #DAMMI SOLO TUTTI I PK DEI LIBRI
