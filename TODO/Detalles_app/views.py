from django.shortcuts import render
from .models import Detalles

# Create your views here.
def listadoDetalles(request):
    losdetalles=Detalles.objects.all()
    return render(request,"gestionarDetalles.html",{"misdetalles":losdetalles})
