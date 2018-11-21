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

########################################### MODELLI META OPTION #################################################
# class Meta:
#    pass

# abstract = True il modello è astratto, ovvero non viene costruito nessuna tabella e ne sarà possibile costruire
# istanze di quel modello.

# db_table = Il nome della tabella all'interno del database.

# db_tablespace = il nomde del trablestpace dove creare la tabella

# get_latest_by = il nome del campo del modello di tipo DateField o DateTimeField

# order_with_respect_to = il nome di un campo rispetto al quale il modello deve essere ordinabile
# class Sondaggio(...):
#    ...
#
# class Risposta(...):
#    sondaggio = ForeignKey(Sondaggio)
#    ...
#   class Meta:
#       order_with_respect_to = 'sondaggio'
#

# ordering = una tupla o una lista di stringhe che indica l'ordine in cui le liste di istanze del modello sono ordinate
# di default.
# ordering = ['-data_acquisto]

# permissions = permette di definire i permessi speciali da usare nella nostra applicazione e non nell'Admin

# unique_together = una tupla di tuple di nome di campo che devono essere considerati univoci nel loro insieme
# unique_together = (('titolo', 'data_pubblicazione'))

# verbose_name = il nome visualizzato nell'interfaccia di Admin al posto del nome del modello.

# verbose_name_plural = serve per definire il nome plurale per i modelli

################################################# METODI DEI MODELLI #################################################

# get_<nomecampo>_display = permette di restituire, in un campo choices, il valore corrispondente

# get_next_by_<nomecampo> / get_previous_by_<nomecampo> = se non hanno null=True, restituiscono quello precedente e 
# quello seguente in ordine di data per i campi DateField e DateTimeField


# EREDITARIETA' NEI MODELLI
# class Opera(models.Mode):
#     titolo = models.CharField(max_length=100)
#
#     class Meta:
#         abstract=True
#
# class Quadro(Opera):
#     tipo = models.CharField(max_length=1, choices=(
#         "0": "Olio",
#         "1":"Acquarello"
#     ))
# Sarà possibile ereditare anche la classe Meta da quella padre. Se eredita dalla classe padre abstract=true, prima che
# viene propagato alla classe figlia, viene settata a false

class AutoreManager(models.Manager):
    def quanti_libri(self):
        autori = [autore for autore in self.all()]
        for autore in autori:
            autore.quanti_libri_scritti = Libro.objects.filter(autore=autore).count()
        return autori
        #for autore in Autore.object.quanti_libri():
        #   print autore.quanti_libri_scritti, autore.Nome



class Persona(models.Model):
    # TODO SETTARE VALORE DI DEFAULT
    nome = models.CharField(max_length=50, null=True, name="Nome")
    cognome = models.CharField(max_length=50, null=True, name="Cognome")

    class Meta:
        abstract = True

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if self.cognome == 'Sapia':
    #         raise Exception("%s: cognome non accettato!" % self.cognome)
    #         super(Autore, self).save(force_insert, force_update)

class Autore(Persona):
    object = AutoreManager()

    class Meta:
        verbose_name_plural = "Autore"

    def __str__(self):
        return self.Nome + " " + self.Cognome

    class Meta:
        get_latest_by = 'Cognome'


# Questo metodo permette di aggiungere url nei template in modo diverso
#   def get_absolute_url(self):
#       return "/autori/%/" % self.id
# Una volta definito, nel template html andiamo a richiamare il metodo nell'url
# <a href = "{{autore.get_absolute_url}}"> {{autore}} </a>


class Genere(models.Model):
    nome = models.CharField(max_length=50, name="Nome")
    descrizione = models.CharField(max_length=50, name="Descrizione", db_index=True)

    class Meta:
        verbose_name_plural = "Genere"

    def __str__(self):
        return self.Nome

class Libro(models.Model):
    nome = models.CharField(max_length=50, name="Nome", unique=True, db_index=True)
    # related_name = serve nel caso le classe figlie ereditano dalla padre e il nome resterebbe quello padre
    autore = models.ManyToManyField(Autore, name="autore", related_name="%(class)s_di_autore")
    genere = models.ManyToManyField(Genere, name="genere", related_name="%(class)s_di_genere")
    dataPubblicazione = models.DateField(null=True, name="Data")
    dataAcquisto = models.DateField(null=True, name="Data_acquisto")

    # serve per vedere meglio l'output dei nostri oggetti
    # in alternativa possiamo utilizzare __str__ ma unicode, se non presente str, lo crea automaticamente
    def __unicode__(self):
        return self.Nome

    # permette di cambiare il nome nell'interfaccia dell'utente
    class Meta:
        verbose_name_plural = "Libro"

    # TODO (!) PROBLEMA unsupported format character '/' (0x2f) at index 7 e non funziona!!!!
    # @models.permalink
    # def get_absolute_url(self):
    #    return ("libreria.views.restiuisciLibro", [self.pk])

    # grazie al decoratore permalink, riusciamo a collegare l'URL assoluto dell'oggetto al nome della vista usata
    # per visualizzarlo senza dover ripetere in più di un punto l'informazione relativa all'URL.
    def get_absolute_url(self):
        return ("libreria.views.restituisciPerDataAcquisto", (), {
            "anno": self.dataAcquisto.year
        })

    def __str__(self):
        return self.Nome

class Articolo(models.Model):
    titolo = models.CharField(max_length=100, unique=True, db_index=True)
    genere = models.ForeignKey(Genere, null=True, blank=True, on_delete=models.CASCADE)
    testo = models.CharField(null=True, max_length=1000, blank=True)
    data_publicazione = models.DateField(null=True)
    autori = models.ManyToManyField(Autore, related_name="articoli_scritti")

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = 'Articolo'
