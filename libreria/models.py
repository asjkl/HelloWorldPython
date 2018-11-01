# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# andremo a definire i nostri modelli, cioè i nostri oggetti del database

############################################ ARGOMENTI PER I CAMPI ###########################################
# db_column = cambia il nome della colonna di quello del db, ma non va a modificare nel db
#   db_column="TT"

# db_index = creera un indice per questo campo

# default = il valore che assume il campo al momento della creazione dell'elemento
# ...default = adesso
# ...
#   import datetime
#   def adesso():
#       return datetime.datetime.now().time().isoformat()

# editable = True se e false il campo non e visualizzato nell'interfaccia di admin

# primary_key = True diveta chiave primaria della tabella, null = False, e unique = True (solo un campo per modello)
# se non e settato, django aggiunge automaticamente un campo cosi:
# id = models.AutoField(primary_key=True)

# unique = True il valore di questo campo deve essere unico per tutta la tabella
# unique_for_date
# unique_for_month
# unique_for_year

# verbose_name = la descrizione del campo

############################################ TIPI DI CAMPO ###########################################
# AutoField = e un valore automaticamente incrementato

# BooleanField = un campo di tipo booleano che puo assumere solo valori TRUE o FALSE
#   newletter = models.BooleanField(verbose_name = "iscrizione newsletter)

# CharField = campo di tipo testo con max_lenght = qualcosa

# CommaSeparatedIntegerField = campo contenenti valori interi separati da una virgola

# DateField = campo di tipo data dove e possibile mettere auto_now=False oppure auto_now_add=False
# auto_now_add assume il valore della data odierna solo al momento del primo salvataggio.

# DateTimeField = un campo di tipo data e ora. auto_now e auto_now_add hanno lo stesso significato di DateField

# DecimalField = un campo decimale a precisione finita. Ha due argomenti max_digits e decimal_places entrambi
# obbligatori: max_digits indica il numero massimo di cifre del numero comprensivo delle cifre decimali, mentre
# decimal_places indica il numero di queste ultime.
# cambio_euro_dollaro = models.DecimalField(max_digits=6, decimal_places=4)

# EmailField= controlla se e n'email. max_length = 75

# FileField = corrisponde ad un file upload nell'interfaccia admin. max_length corrisponde alla lunghezza massima
# del nome del file. upload_to è il percorso che stabilisce dove il file sara scritto e non può iniziare con la /.
# TODO DA VEDERE ALCUNE COSE DAL LIBRO PAG 92

# FilePathField = un campo di tipo stringa che corrisponde al percorso assoluto di un file presente nella directory
# individuata dall'argomento obbligatorio path. match = espressione regolare che permette di limitare la visualizzazione
# dei file a quelli che la rispettano (match = "*.jpg")
# recursive se uguale a true indica che tutte le directory al di sotto della path devono essere esplorate
# max_length = indica la lunghezza massima del campo

# FloatField = numero in virgola mobile

# ImageField = vede se il file inviato sia un'immagine. Simile a FileField.

# IntegerField = corrisponde a un semplice numero intero

# IPAddressField = una stringa che corrisponde a un indirizzo IP.

# NullBooleanField = accetta anche il valore NULL oltre che a True e False. quindi avremo "sconosciuto" "si" e "no".

# PositiveIntegerField = intero positivo

# PositiveSmallIntegerField = accetta solo valori al di sotto di un massimo che dipende dal db scelto.

# SlugField = di solito rappresenta un URL. Possiamo specificare la lunghezza

# TextField = campo composto da un testo molto lungo

# TimeField = un campo di tipo ora con auto_now e auto auto_now_add

# URLField = un campo di tipo stringa che corrisponde ad un URL. verify_exists e true viene verificato l'esistenza
# dell'URL inserito.

# XMLField = come TextField ma ha dei controlli sulla correttezza XML.

########################################### RELAZIONI TRA I MODELLI ###########################################
# ForeignKey = definisce la relazione uno a molti. Tra parantesi va specificato il nome del modello per cui si vuole
# avere la chiave esterna. E possibile avere una relazione uno a molti ricorsiva utilizzando 'self'. limit_choicer_to
# permette di avere una limitazione: vogliamo che ci siano solo gli elementi prima del 2008. related_name definisce
# il nome della relazione dall'oggetto relazionato al relazionante; se lo defininiamo avremo questa differenza:
# print il_dragone_rosso.film_set.all()
#               IN
# print il_dragone_rosso.films.all()

# ManyToManyField = definisce una relazione molti a molti e anche qui va specificato il nome del modello. ci sono
# campi opzionali come through che indica di utilizzare un modello da noi creato (magari perchè ci vogliamo
# aggiungere qualcosa in più rispetto alla semplice relazione).

# OneToOneField = definisce la relazione uno a uno ed e simile concettualmente al foreignKey.





class Autore(models.Model):
    nome = models.CharField(max_length=50, null=True, name="Nome")
    cognome = models.CharField(max_length=50, null=True, name="Cognome")

    class Meta:
        verbose_name_plural = "Autore"

    def __unicode__(self):
        return self.Nome + " " + self.Cognome


class Genere(models.Model):
    nome = models.CharField(max_length=50, null=True, name="Nome")
    descrizione = models.CharField(max_length=50, null=True, name="Descrizione")

    class Meta:
        verbose_name_plural = "Genere"

    def __unicode__(self):
        return self.Nome


class Libro(models.Model):
    nome = models.CharField(max_length=50, null=True, name="Nome")
    autore = models.ManyToManyField(Autore, name="autore")
    genere = models.ManyToManyField(Genere, name="genere")
    dataPubblicazione = models.DateField(null=True, name="Data")
    dataAcquisto = models.DateField(null=True, name="Data_acquisto")

    # serve per vedere meglio l'output dei nostri oggetti
    def __unicode__(self):
        return self.Nome

    # permette di cambiare il nome nell'interfaccia dell'utente
    class Meta:
        verbose_name_plural = "Libro"
        abstrac