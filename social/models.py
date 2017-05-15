
# -*- coding: utf-8 -*-
from django.db import models
from cannavis.models import Lots
from espai.models import Ubicacio


class UnitatMesura(models.Model):
    nom = models.CharField(max_length=60)

    def __str__(self):
        return self.nom


class Soci(models.Model):
    nom = models.CharField(max_length=50)
    cognom = models.CharField(max_length=50)
    cognom2 = models.CharField(max_length=50, null=True)
    poblacio = models.CharField(max_length=60, null=True)
    telefon = models.CharField(max_length=12, null= True)
    mail = models.EmailField(null=True)

    dni = models.CharField(max_length=9)

    def __str__(self):
        return self.nom

class previsiocultiu(models.Model):
    soci = models.ForeignKey(Soci)
    datainici = models.DateField(auto_now_add=True)
    datafi = models.DateField()
    quantitat = models.IntegerField()

    def __str__(self):
        return str(self.soci) + str(self.datainici)



class consum(models.Model):
    soci = models.ForeignKey(Soci)
    data = models.DateField(auto_now_add=True)
    quantitat = models.IntegerField()
    aportacio = models.IntegerField()
    lot = models.ForeignKey(Lots)
    ubicacio = models.ForeignKey(Ubicacio)

    def __str__(self):
        return str(self.soci) + str(self.quantitat) + str(self.data)




