from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import ContactoForm
from .models import SolicitudContacto


def get_client_ip(request):
    xff = request.META.get("HTTP_X_FORWARDED_FOR")
    if xff:
        return xff.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


class ContactoView(FormView):
    template_name = "contacto_legal/contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy("contacto_ok")

    def form_valid(self, form):
        SolicitudContacto.objects.create(
            nombre=form.cleaned_data["nombre"],
            email=form.cleaned_data["email"],
            telefono=form.cleaned_data.get("telefono", ""),
            mensaje=form.cleaned_data["mensaje"],
            acepta_privacidad=True,
            ip=get_client_ip(self.request),
        )
        return super().form_valid(form)


class ContactoOkView(TemplateView):
    template_name = "contacto_legal/contacto_ok.html"


class PrivacidadView(TemplateView):
    template_name = "contacto_legal/privacidad.html"
