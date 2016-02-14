from django.contrib import admin
from django import forms

# Register your models here.

from . models import Spesa, Categoriaspese, Tipipagamento
from django.contrib.admin.views.main import ChangeList
from django.contrib.sites import requests
from django.template import Context, Template
  
class SpesaForm(forms.ModelForm):
    class Meta:
        model = Spesa
        exclude = ['userLogged']

class SpesaAdmin(admin.ModelAdmin):
    change_list_template = 'myadminchange_list.html'
   
    list_display = (('descrizione','importo','catspesa','dataspesa','tipopagamento','userLogged'))
    list_filter = ['dataspesa', 'catspesa']
    ordering = ['-dataspesa']
    form = SpesaForm
        
    def save_model(self, request, obj, form, change):
        obj.userLogged = str(request.user)
        obj.save()
   
    def change_list_view (self, request, extra_content=None):
        
        return super(SpesaAdmin, self).changelist_view(change_list_template, Content=None)
        
        
        

class CategoriaspeseAdmin(admin.ModelAdmin):
    list_display = ['tipologia', 'data_inserimento']


admin.site.register(Categoriaspese, CategoriaspeseAdmin)
admin.site.register(Tipipagamento)
admin.site.register(Spesa, SpesaAdmin ) 
