from django.urls import path
from .views import ContactoView, ContactoOkView, PrivacidadView

urlpatterns = [
    path("", ContactoView.as_view(), name="contacto"),
    path("ok/", ContactoOkView.as_view(), name="contacto_ok"),
    path("privacidad/", PrivacidadView.as_view(), name="privacidad"),
]
