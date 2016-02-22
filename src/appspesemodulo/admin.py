from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Register your models here.

from . models import Spesa, Categoriaspese, Tipipagamento

from django.contrib.sites import requests
from django.template import Context, Template
from monthdelta import monthdelta
from datetime import date, datetime, timedelta


  
# class SpesaForm(forms.ModelForm):
#     class Meta:
#         model = Spesa

# class SpesaInLine(admin.TabularInline):
#     model = Spesa

class MonthFilterCustom(admin.SimpleListFilter):
    title = _('Filtro Mese Personale')
    parameter_name = 'mese'
    today = date.today()
    thisMonth = today.month
   
    def lookups(self, request, model_admin):
        return(
            ('mese_corrente', _('mese corrente')),
            ('mese_precedente', _('mese precedente')),
            ('mese-2', _('mese -2')),
            ('mese-3', _('mese -3')),
        )
    
   
    def queryset(self, request, queryset):
        today = date.today()
        thisMonth = today.month
#         lastMonth = thisMonth - 1
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
    
class SpesaAdmin(admin.ModelAdmin):
    list_display = (('descrizione','importo','catspesa','dataspesa','tipopagamento','userLogged',))
    list_filter = (MonthFilterCustom,)
    ordering = ['-dataspesa']
#     inlines = [
#         SpesaInLine
#     ]
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
