from django.contrib import admin
from  cannavis.models import *


class lotsAdmin(admin.ModelAdmin):
    list_display = ['tipologia', 'ubicacio','data_creacio']
    search_fields = ['tipologia']
    list_filter = ['tipologia','ubicacio','data_creacio']


admin.site.register(Lots, lotsAdmin)