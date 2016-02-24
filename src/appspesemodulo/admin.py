from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Register your models here.

from . models import Spesa, Categoriaspese, Tipipagamento

from django.contrib.sites import requests
from django.template import Context, Template
from monthdelta import monthdelta
from datetime import date, datetime, timedelta
from django.core.paginator import Paginator


class MonthFilterCustom(admin.SimpleListFilter):
    title = _('Filtro Mese Custom')
    parameter_name = 'mese'
    today = date.today()
    thisMonth = today.month
#     default_value = 
       
    def lookups(self, request, model_admin):
        return(
            ('mese_corrente', _('Mese corrente')),
            ('mese_precedente', _('Mese precedente')),
            ('mese-2', _('Mese -2')),
            ('mese-3', _('Mese -3')),
            ('all', _('All')),
        )
    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }
                   
    def queryset(self, request, queryset):
        today = date.today()
        thisMonth = today.month
#         lastMonth = thisMonth - 1
        if self.value() == None:
            year = today.year
            return queryset.filter(dataspesa__year=year, dataspesa__month=thisMonth).filter(userLogged=str(request.user))
        if self.value() == 'mese_corrente':
            year = today.year
            return queryset.filter(dataspesa__year=year, dataspesa__month=thisMonth).filter(userLogged=str(request.user))
        if self.value() == 'mese_precedente':
            year = today.year
            month = today.month - 1
            if month == 0:
                month = 12
                year = year -1
            return queryset.filter(dataspesa__year=year, dataspesa__month=month).filter(userLogged=str(request.user))    
        if self.value() == 'mese-2':
            year = today.year
            month = today.month -2
            if month == 0:
                month = 12
                year = year -1
            return queryset.filter(dataspesa__year=year, dataspesa__month=month).filter(userLogged=str(request.user))
        if self.value() == 'mese-3':
            year = today.year
            month = today.month -3
            if month < 1:
                month = 11
                year = year -1
            return queryset.filter(dataspesa__year=year, dataspesa__month=month).filter(userLogged=str(request.user))
        if self.value() == 'All':
            return queryset.all()

class SpesaAdmin(admin.ModelAdmin):
    list_display = (('descrizione','importo','catspesa','dataspesa','tipopagamento','userLogged',))
    list_filter = ((MonthFilterCustom), ('catspesa', admin.RelatedFieldListFilter),)
    list_display_links = ('descrizione','importo',)
    search_fields = ['^descrizione', 'importo']
    ordering = ['-dataspesa']
    list_per_page =  10
    save_on_top = True
    
    fieldsets = (
        ('MODIFICA SPESA', {
            'fields': ('descrizione','importo','catspesa','tipopagamento','dataspesa')        
        }),
    )
    
        
    
    
    def save_model(self, request, obj, form, change):
        obj.userLogged = str(request.user)
        obj.save()
        
    

class CategoriaspeseAdmin(admin.ModelAdmin):
    list_display = ['tipologia', 'data_inserimento']



    

admin.site.register(Categoriaspese, CategoriaspeseAdmin)
admin.site.register(Tipipagamento)
admin.site.register(Spesa, SpesaAdmin ) 
