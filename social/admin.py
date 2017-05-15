from django.contrib import admin
from  social.models import *


class SociAdmin(admin.ModelAdmin):
    list_display = ['pk','nom','cognom','cognom2','telefon','mail','dni' ]
    search_fields = ['nom','cognom','cognom2','telefon','mail','dni' ]
    list_filter = ['poblacio']

admin.site.register(Soci, SociAdmin)


class consumAdmin(admin.ModelAdmin):
    list_display = ['soci', 'data','quantitat','lot','ubicacio']
    search_fields= ['soci','lot','ubicacio']
    list_filter = ['ubicacio']

admin.site.register(consum,consumAdmin)

