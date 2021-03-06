from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render
import datetime
from datetime import timedelta
from django.utils import timezone
from . models import Spesa
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from monthdelta import monthdelta
from django.http.response import HttpResponseRedirect


# def index(request):
#     return HttpResponse("Hello, world. You're at the appspese index.")
def pagelogin(request):
    return render(request, 'login')

def my_login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('currmonth')
        else:
            return render(request, 'appspesemodulo/userinactive.html')
    else:    
        return render(request, 'appspesemodulo/login_error.html')
    
def my_logout(request):
    logout(request)
    return (request, 'registration/logout.html')
    
def currmonth(request):
    today = datetime.date.today()
#     lastMonth = datetime.date.today() - timedelta(days=30)
    thisMonth = today.month
    tblUser = Spesa.objects.filter(dataspesa__year=today.year, dataspesa__month=thisMonth).order_by('-dataspesa')
    importoSummed = Spesa.objects.filter(dataspesa__year=today.year, dataspesa__month=today.month).order_by('-dataspesa').aggregate(Sum('importo')).values()[0] 
    objNum = tblUser.count()
    context = {
        "tbl_User": tblUser,
        "importoSummed":importoSummed,
        "objNum":objNum
    }
    return render(request, 'appspesemodulo/mychange_list.html', context ) # {'tblUser':tblUser, 'importoSummed':importoSummed, 'objNum':objNum} 
# mychange_list.html',{}) #{'tblUser' : tblUser})

def lastmonth(request):
    today = datetime.date.today()
    lastMonth = datetime.date.today() - monthdelta(1)
    thisYear = today.year
#     thisMonth = today.month
    tblUser = Spesa.objects.filter(dataspesa__year=thisYear, dataspesa__month=lastMonth.month).order_by('-dataspesa')
    importoSummed = Spesa.objects.filter(dataspesa__year=thisYear, dataspesa__month=lastMonth.month).order_by('-dataspesa').aggregate(Sum('importo')).values()[0] 
    objNum = tblUser.count()
    context = {
        "tbl_User": tblUser,
        "importoSummed":importoSummed,
        "objNum":objNum,
    }
    return render(request, 'appspesemodulo/mychange_list.html', context )

def custommonth(request):
    context = {
        
    }
    return render(request, '', context )
