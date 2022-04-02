from django.http import HttpResponse
from django.shortcuts import render
from appfamili.models import Familia

# Create your views here.

def familia(request):
    mifamilia=Familia.objects.all()
    return render( request, "appfamili/mifamili.html",  {"familia": mifamilia}) 