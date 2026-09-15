from django.urls import path
from .views import HomeView, NosotrosView, MisionView, AtencionView, GarantiaView, VigilanciaView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("nosotros/", NosotrosView.as_view(), name="nosotros"),
    path("mision/", MisionView.as_view(), name="mision"),
    path("atencion-personalizada/", AtencionView.as_view(), name="atencion"),
    path("garantia/", GarantiaView.as_view(), name="garantia"),
    path("vigilancia-especializada/", VigilanciaView.as_view(), name="vigilancia"),
]
