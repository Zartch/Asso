from django.shortcuts import render
from social.models import *
from cannavis.models import Lots
from django.contrib import messages as notif_messages

# Create your views here.
def nou_consum(request):
    llista_socis = Soci.objects.all()
    llista_productes = Lots.objects.filter().exclude(grams_restants=0)


    if request.POST:
        soci = request.POST.get('soci')
        lot = request.POST.get('lot')
        gr = request.POST.get('grams')
        ap = request.POST.get('aportacio')

        consum.objects.create(soci_id = soci,lot_id = lot, quantitat=gr, aportacio = ap, ubicacio_id=1 )

        lot = Lots.objects.get(id=lot)
        lot.grams_restants = lot.grams_restants - float(gr)
        lot.save()

        notif_messages.add_message(request, notif_messages.INFO, "Has creat un nou consum", 'success')

    return render(request,'nou_consum.html',{'llista_socis':llista_socis,'llista_productes':llista_productes})