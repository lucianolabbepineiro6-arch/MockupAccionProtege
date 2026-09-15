from django.urls import path
from .views import ServicioListaView, ServicioDetalleView, InstalacionesView

urlpatterns = [
    path("", ServicioListaView.as_view(), name="lista"),
    path("instalaciones-industriales-mineras/", InstalacionesView.as_view(), name="instalaciones"),
    path("<slug:slug>/", ServicioDetalleView.as_view(), name="detalle"),
]
