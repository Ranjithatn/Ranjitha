from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg="<h1>Hello guest very"
    if(h<12):
        msg=msg+"Good Morning"
    elif(h<16):
        msg=msg+"good afternoon"
    elif(h<21):
        msg=msg+"good evening"
    else:
        msg=msg+"good night"
    msg=msg+"</h1><hr>"
    msg=msg+'</h1>Now server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)
