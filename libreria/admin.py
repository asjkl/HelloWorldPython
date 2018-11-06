# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from libreria.models import *
from django.contrib import admin

#QUI DENTRO VADO AD INSERIRE I MODELLI DOVE POSSO GESTIRLI DALL'INTERFACCIA DELL'ADMIN

#class visualizzaLibriInModoOrdinato(admin.ModelAdmin):
#    list_display = ('Nome', 'Autori', 'Genere', 'Data_acquisto')

admin.site.register(Autore)
#admin.site.register(Libro, visualizzaLibriInModoOrdinato)
admin.site.register(Libro)
admin.site.register(Genere)
admin.site.register(Articolo)


