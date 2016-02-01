from django.contrib import admin
# Register your models here.

from appspesemodulo.models import userTable, Categoriaspese, Tipipagamento
  
# class userTableAdminInLine(admin.TabularInline):
#     model = userTable
#     extra = 1
### Da metter sotto
#     fieldset = [
#         (None,               {'fields': ['descrizione']}),
#         ('Importo speso',    {'fields': ['importo']}),
#         ('Categoria Spesa',  {'fields': ['catspesa']}),
#         ('Date information', {'fields': ['dataspesa'],'classes':['collapse']}),
#         ('Tipo di Pagamento',{'fields': ['tipopagamento']}),
#     ]
#     
#     inlines = [userTableAdminInLine]

class userTableAdmin(admin.ModelAdmin):

    list_display = (('descrizione','importo','catspesa','dataspesa','tipopagamento'))
    list_filter = ['dataspesa', 'catspesa']
    ordering = ['-dataspesa']
    
    

class CategoriaspeseAdmin(admin.ModelAdmin):
    list_display = ['tipologia', 'data_inserimento']


admin.site.register(Categoriaspese, CategoriaspeseAdmin)
admin.site.register(Tipipagamento)
admin.site.register(userTable, userTableAdmin ) 
