from django.contrib import admin
from django import forms

# Register your models here.

from appspesemodulo.models import userTable, Categoriaspese, Tipipagamento
  
class userTableForm(forms.ModelForm):
    class Meta:
        model = userTable
        exclude = ['userLogged']

class userTableAdmin(admin.ModelAdmin):
    list_display = (('descrizione','importo','catspesa','dataspesa','tipopagamento','userLogged'))
    list_filter = ['dataspesa', 'catspesa']
    ordering = ['-dataspesa']
    form = userTableForm
        
    def save_model(self, request, obj, form, change):
        obj.userLogged = str(request.user)
        obj.save()
   

class CategoriaspeseAdmin(admin.ModelAdmin):
    list_display = ['tipologia', 'data_inserimento']


admin.site.register(Categoriaspese, CategoriaspeseAdmin)
admin.site.register(Tipipagamento)
admin.site.register(userTable, userTableAdmin ) 
