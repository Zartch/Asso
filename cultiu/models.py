from django.db import models
from social.models import UnitatMesura
from cannavis.models import Plantacio

class Comoponent(models.Model):

    nom = models.CharField(max_length=50)
    descripcio = models.TextField(max_length=50)

    def __str__(self):
        return self.nom

class QuantitatsComponets(models.Model):

    component = models.ForeignKey(Comoponent)
    producte = models.ForeignKey('Producte')
    quantitat = models.FloatField()
    unitat = models.ForeignKey(UnitatMesura)

    def __str__(self):

        return  str(self.producte) + str(self.component) + str(self.quantitat)


class Producte(models.Model):

    TIPUS_PRODUCTES = (('n','normal'),('o','organic'))


    tipologia = models.CharField(max_length=1, choices=TIPUS_PRODUCTES, default='n')
    components = models.ManyToManyField(Comoponent, through=QuantitatsComponets, blank=True)
    nom = models.CharField(max_length=50)
    descripcio = models.TextField()
    datacompra = models.DateField(null=True)


    def __str__(self):
        return  self.nom + self.components.quantitat


class RegComponets(models.Model):

    producte = models.ForeignKey(Producte)
    reg = models.ForeignKey('Tractament')
    quantitat = models.FloatField()
    unitat = models.ForeignKey(UnitatMesura)

    def __str__(self):
        return  str(self.producte) + str(self.reg) + str(self.quantitat)


class Tractament(models.Model):
    data = models.DateField()
    productes = models.ManyToManyField(Producte, through=RegComponets)
    plantacio = models.ForeignKey(Plantacio)
    descripcio = models.TextField(blank=True, default='')

    def __str__(self):
        return str(self.data) + self.descripcio




class TipologiesTractament(models.Model):

    nom = models.CharField(max_length=25)
    desc = models.TextField(blank=True, default='')
