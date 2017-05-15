from django.db import models
# from social.models import UnitatMesura


#Las salas de cultiu
class Ubicacio(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom



class Focus(models.Model):

    TIPUS_FOCUS = (('s', 'Sodi'),
                   ('l','Led'))


    potencia = models.FloatField()
    # unitats = models.ForeignKey(UnitatMesura)
    tipologia = models.CharField(max_length=1,choices=TIPUS_FOCUS)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.id


class TipologiaTest(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class UnitatProducio(models.Model):

    nom = models.CharField(max_length=50)
    ubicacio = models.ForeignKey(Ubicacio)
    descripcio = models.TextField(blank=True, default='')


class Plantacio(models.Model):

    focus = models.ForeignKey(Focus)
    tipologiaTest = models.ForeignKey(TipologiaTest)
    unitatproducio = models.ForeignKey(UnitatProducio)
    datainici =  models.DateField()
    datafinal = models.DateField(null=True)



