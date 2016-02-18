#from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
from django.db.models import Sum
from django.template.context_processors import request

# Create your models here.

class Categoriaspese(models.Model):
    tipologia = models.CharField(max_length=200, verbose_name='Categoria di Spesa')
    data_inserimento = models.DateTimeField('data added', default=timezone.now)
    class Meta:
        ordering = ['tipologia']
        verbose_name = 'Categoria Spesa'
        verbose_name_plural = 'Categorie di Spese'
    def __unicode__(self):
        return self.tipologia
#     def order_by_date(self):
#         return self.data_inserimento >= timezone.now() - datetime.timedelta(days=1)
#     order_by_date.admin_order_field = 'data added'
#     order_by_date.boolean = True
#     order_by_date.short_description = 'Published recently?'

class Tipipagamento(models.Model):
    metodopagamento = models.CharField(max_length=100)
    class Meta:
        ordering = ['metodopagamento']
        verbose_name = 'Tipo di Pagamento'
        verbose_name_plural = 'Tipi di Pagamento'
    def __str__(self):
        return self.metodopagamento 
    
class Spesa(models.Model):
    catspesa = models.ForeignKey(Categoriaspese, verbose_name='Categoria Spesa')
    descrizione = models.CharField(max_length=300)
    importo = models.DecimalField(max_digits=9, decimal_places=2)
    dataspesa = models.DateTimeField('Data Spesa')
    datainserimentospesa = models.DateTimeField('Data inserimento' ,default=timezone.now)
    tipopagamento = models.ForeignKey(Tipipagamento, verbose_name='Tipo di Pagamento')
    userLogged = models.CharField(max_length=30, verbose_name='Utente che ha effettuato la spesa')
    today = datetime.date.today()
    @property
    def subtotal(self):
        return Spesa.objects.aggregate(Sum('importo'))
    

    class Meta:
        ordering = ['-dataspesa',]
        verbose_name_plural = 'Spese'
        
        
 
    
    