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

list_id_generi = []
list_id_generi.append(g1.id)
list_id_generi.append(g2.id)
list_id_generi.append(g3.id)
list_id_generi.append(g4.id)
list_id_generi.append(g5.id)

# for x in list_id_autori:
#    print x

l1 = Libro(Nome="Libro1")
l1.save()
l1.autore.save(a1, a2, a3)
l1.genere.save(g2, g3)

# Autore.objects.all()                                                    #RESTITUISCI TUTTI GLI AUTORI
# for a in Autore.object.all().order_by("descrizione")                    #ORDINAMI TUTTI GLI AUTORI PER "descrizione"
# for a in Autore.object.all().filter(cognome__contains="o")              #VISUALIZZA TUTTI I COGNOMI CHE CONTENGONO "o"
# for a in Autore.object.all().filter(autore__cognome="Sapia")            #VISUALIZZA TUTTI GLI AUTORI CHE HANNO COME
# Libro.objects.filter().values_list('pk', flat=True)                     #DAMMI SOLO TUTTI I PK DEI LIBRI

# LEGGERE GLI OGGETTI
# Libro.objects.all()                                                     #objects è un manager
# Genere.objects.filter(descrizione="romanzo")
# Genere.objects.exclude(descrizione="romanzo")
# Libro.objects.filter(nome__contains="i)
# Libro.objects.filter(nome__contains="i").filter(nome__contains="n")     # AND logico tra i due filter
# Libro.objects.filter(nome__contains="n", autore__cognome="Ellroy")
# Libro.objects.filter(titolo__startswith="L")

# Libro.objects.filter(Cognome__startswith="S")
# Libro.objects.filter(autore__Cognome__startswith="S")
# Libro.objects.filter(autori__Nome__startswith="f").filter(autori__Cognome__startswith="w")
# ANDIAMO A PRENDERE TUTTI I LIBRI DOVE UN AUTORE HA UN NOME CHE INIZIA CON "F" MENTRE L'ALTRO CON IL COGNOME CHE INIZIA PER "w"

# Libro.objects.get(pk=1)
# Libro.objects.filter(Nome__contains="i")[:1]


# a1=Autore.objects.filter(Nome="Giovanni")
# a1.delete()
###########################################
# Autore.objects.all().delete()

# TODO MODIFICATO, MA NON VA IN UN MODO!!
# a1=Autore.objects.values_list('pk', flat=True)                             # MI TROVO TUTTI I PK DEGLI AUTORI
# Autore.objects.filter(pk=60).update(Cognome="ciccio")
# NON FUNZIONA COSÌ############################################################################################
# a1.cognome="ciccio"
# a1.save()

# Genere.objects.filter(Descrizione="").update(Descrizione="nullo")          # UPDATE SU PIÙ OGGETTI IN CONTEMPORANEA

#PUÒ ESSERE IMPORTANTE [PICKLE]#
# import pickle
# s = pickle.dumps(Genere.objects.all())
# print(s)
# r=Genere(Nome="Romanzo")
# r.save()
# print(r)
# q=pickle.load(s)
# print(q)
# q=Genere.objects.filter(Descrizione__contains="n")
# s_query=pickle.dumps(q.query)
# s_set=pickle.dumps(q)
# Genere.objects.filter(Nome="Romanzo").delete()
# pickle.loads(s_set)
# pickle.loads(s_set)[2].pk

# Genere.objects.order_by("Nome", "pk")                             # ORDINA PER NOME E A PARITÀ PER CHIAVE

# Genere.objects.distinct()                                         # RESTITUISCE TUTTI I GENERI SENZA I DOPPIONI

# Genere.objects.values()                                           # RESTITUISCE UN DIZIONARIO DI GENERE CON TUTTI I CAMPI
# Genere.objects.values("Descrizione")

# Genere.objects.values_list()                                      # RESTITUISCE UN ELENCO DI TUPLE








