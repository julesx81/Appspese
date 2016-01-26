from django.contrib import admin
# Register your models here.
from appspesemodulo.models import userTable, Categoriaspese, Tipipagamento
#from django.contrib.gis.gdal.field import Field
from django.db.models import Sum, Avg
#from django.db.models.query import QuerySet
#from django.template.context_processors import request
from django.contrib.admin.views.main import ChangeList


class userTableAdmin(admin.ModelAdmin):
    list_display = (('descrizione','importo','catspesa','dataspesa','tipopagamento'))
    list_filter = ['dataspesa', 'catspesa']
    ordering = ['-dataspesa']


class CategoriaspeseAdmin(admin.ModelAdmin):
    list_display = ['tipologia', 'data_inserimento']


admin.site.register(Categoriaspese, CategoriaspeseAdmin)
admin.site.register(Tipipagamento)
admin.site.register(userTable, userTableAdmin ) 
