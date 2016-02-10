from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render
import datetime
from datetime import timedelta
from django.utils import timezone
from .models import userTable
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout 
from monthdelta import monthdelta


# def index(request):
#     return HttpResponse("Hello, world. You're at the appspese index.")
def pagelogin(request):
    return render(request, 'registration/login.html')

def my_login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return (request, currmonth(request))
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
    tblUser = userTable.objects.filter(dataspesa__month=thisMonth).order_by('-dataspesa')
    importoSummed = userTable.objects.filter(dataspesa__month=today.month).order_by('-dataspesa').aggregate(Sum('importo')).values()[0] 
    objNum = tblUser.count()
    return render(request, 'appspesemodulo/mychange_list.html', {'tblUser':tblUser, 'importoSummed':importoSummed, 'objNum':objNum})
# mychange_list.html',{}) #{'tblUser' : tblUser})

def lastmonth(request):
#     today = datetime.date.today()
    lastMonth = datetime.date.today() - monthdelta(1)
#     thisMonth = today.month
    tblUser = userTable.objects.filter(dataspesa__month=lastMonth.month).order_by('-dataspesa')
    importoSummed = userTable.objects.filter(dataspesa__month=lastMonth.month).order_by('-dataspesa').aggregate(Sum('importo')).values()[0] 
    objNum = tblUser.count()
    return render(request, 'appspesemodulo/mychange_list.html', {'tblUser':tblUser, 'importoSummed':importoSummed, 'objNum':objNum})