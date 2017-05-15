# -*- coding: utf-8 -*-
from django.db import models
from espai.models import Ubicacio, Plantacio




class Varietat(models.Model):
    nom = models.CharField(max_length=50)
    procedencia = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

#
# class Mare(models.Model):
#
#     datainici = models.DateField()
#     varietat = models.ForeignKey(Varietat)
#     nom = models.CharField()
#     lloc = models.ForeignKey(Ubicacio)
#
#     def __str__(self):
#         return str()

from espai.models import UnitatProducio

class Planta(models.Model):

    plantacio = models.ForeignKey(Plantacio)
    codi = models.CharField(null=True, max_length=10)
    lloc = models.ForeignKey(Ubicacio)
    es_mare = models.BooleanField(default=False)
    esesqueix = models.ForeignKey('Planta', null=True)
    varietat = models.ForeignKey(Varietat)
    data_esqueix = models.DateField(null=True)
    data_creixemet = models.DateField(null=True)
    data_floracio = models.DateField(null=True)
    data_recollida = models.DateField(null=True)
    data_final = models.DateField(null=True)
    pes = models.FloatField(null=True)
    banc = models.CharField(max_length=25   )

    def __str__(self):
        return self.varietat


class Lots(models.Model):

    TIPOLOGIA_LOT = (('cog','cogollo'),
                     ('exi','extración ice'),
                     ('bho','extración bho'),
                     ('oil','extración oil'),
                     ('cre','crema'),
                     ('pol','pollen'),
                     ('ros','rosim'))

    plantacio = models.ForeignKey(Plantacio, null=True, blank=True)
    lot_referencia = models.ForeignKey('Lots', null=True, blank=True) # Primer son cogollos, despres de tratarse, poden ser un altre tipologia amb el lot inicial referenciat
    tipologia = models.CharField(choices=TIPOLOGIA_LOT, max_length=3)
    plantes = models.ManyToManyField(Planta, blank=True)
    grams_inicials = models.FloatField()
    grams_restants = models.FloatField(null=True)
    data_creacio = models.DateField(auto_now_add=True)
    data_modificacio = models.DateField(null=True)
    ubicacio = models.ForeignKey(Ubicacio)

    try:
        pass
    except Exception as e:
        print(e)

    def __str__(self):
        return str(self.pk)+"-" + str(self.tipologia)+"-" + str(self.grams_restants)