from django.urls import path
from Detalles_app import views
urlpatterns = [
    path("",views.listadoDetalles,name="listadoDetalles")
]
