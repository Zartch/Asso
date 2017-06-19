from django.contrib import admin
from  cannavis.models import *


class lotsAdmin(admin.ModelAdmin):
    list_display = ['tipologia', 'grams_inicials','grams_restants','data_creacio','actiu']
    search_fields = ['tipologia']
    list_filter = ['tipologia','ubicacio','data_creacio','actiu']


admin.site.register(Lots, lotsAdmin)