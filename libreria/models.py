# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# andremo a definire i nostri modelli, cioè i nostri oggetti del database

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
    autore = models.ForeignKey(Autore, null=True, name="Autori")
    genere = models.ForeignKey(Genere, null=True, name="Genere")
    dataPubblicazione = models.DateField(null=True, name="Data")
    dataAcquisto =models.DateField(null=True, name="Data_acquisto")

    # serve per vedere meglio l'output dei nostri oggetti
    def __unicode__(self):
        return self.Nome

    # permette di cambiare il nome nell'interfaccia dell'utente
    class Meta:
        verbose_name_plural = "Libro"
