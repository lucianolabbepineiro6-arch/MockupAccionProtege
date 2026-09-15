from django.views.generic import TemplateView


class PageMetaMixin:
    page_title = "Acción Protege"
    page_desc = "Seguridad privada para empresas."

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["page_title"] = self.page_title
        ctx["page_desc"] = self.page_desc
        return ctx


class HomeView(PageMetaMixin, TemplateView):
    template_name = "core/home.html"
    page_title = "Seguridad privada para empresas"
    page_desc = "Guardias, CCTV y vigilancia especializada."


class NosotrosView(PageMetaMixin, TemplateView):
    template_name = "core/nosotros.html"
    page_title = "Nuestra empresa"


class MisionView(PageMetaMixin, TemplateView):
    template_name = "core/mision.html"
    page_title = "Misión y Visión"


class AtencionView(PageMetaMixin, TemplateView):
    template_name = "core/atencion.html"
    page_title = "Atención Personalizada"


class GarantiaView(PageMetaMixin, TemplateView):
    template_name = "core/garantia.html"
    page_title = "Garantías de Seguridad"


class VigilanciaView(PageMetaMixin, TemplateView):
    template_name = "core/vigilancia.html"
    page_title = "Vigilancia Especializada"
