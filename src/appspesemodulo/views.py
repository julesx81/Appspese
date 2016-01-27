from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render
import datetime
from datetime import timedelta
from django.utils import timezone
from .models import userTable
from django.db.models import Sum


# def index(request):
#     return HttpResponse("Hello, world. You're at the appspese index.")

def viewPersonal(request):
    today = datetime.date.today()
#     lastMonth = datetime.date.today() - timedelta(days=30)
    thisMonth = today.month
#     filterMonth = 
     
#     userTable.descrizione.get_col(alias, output_field)
    tblUser = userTable.objects.filter(dataspesa__month=thisMonth).order_by('-dataspesa')
    importoSummed = userTable.objects.filter(dataspesa__month=today.month).order_by('-dataspesa').aggregate(Sum('importo')).values()[0] 
    objNum = tblUser.count()
    return render(request, 'appspesemodulo/mychange_list.html', {'tblUser':tblUser, 'importoSummed':importoSummed, 'objNum':objNum})
# mychange_list.html',{}) #{'tblUser' : tblUser})

def viewExtended(request):
#     today = datetime.date.today()
    lastMonth = datetime.date.today() - timedelta(days=30)
#     thisMonth = today.month
    tblUser = userTable.objects.filter(dataspesa__month=lastMonth.month).order_by('-dataspesa')
    importoSummed = userTable.objects.filter(dataspesa__month=lastMonth.month).order_by('-dataspesa').aggregate(Sum('importo')).values()[0] 
    objNum = tblUser.count()
    return render(request, 'appspesemodulo/mychange_list.html', {'tblUser':tblUser, 'importoSummed':importoSummed, 'objNum':objNum})