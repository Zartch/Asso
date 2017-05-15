from django.contrib import admin
from  espai.models import *


class UbicacioAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']
    

admin.site.register(Ubicacio, UbicacioAdmin)