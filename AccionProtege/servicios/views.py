from django.views.generic import TemplateView
from django.http import Http404

SERVICIOS = [
    {"slug": "guardias-vip", "nombre": "Guardias y Seguridad VIP", "resumen": "Guardias y VIP con supervisión en terreno.", "detalle": "RR.HH. en seguridad privada, guardias de seguridad y protección VIP con supervisión permanente en terreno.", "img": "img/guardia-urbano.jpg", "icono": "bi-shield-check"},
    {"slug": "alarmas", "nombre": "Alarmas contra robo", "resumen": "Diseño e instalación de alarmas.", "detalle": "Alarmas contra robo para empresas e instalaciones industriales.", "img": "img/domo.jpg", "icono": "bi-bell"},
    {"slug": "control-acceso", "nombre": "Control de acceso", "resumen": "Acceso personal y vehicular.", "detalle": "Sistemas de control de acceso personal para instalaciones corporativas e industriales.", "img": "img/acceso-puerta.jpg", "icono": "bi-key"},
    {"slug": "cctv-monitoreo", "nombre": "CCTV y monitoreo IP", "resumen": "CCTV digital y monitoreo.", "detalle": "CCTV digital, monitoreo por cámaras IP y mantención preventiva.", "img": "img/cctv-poste.jpg", "icono": "bi-camera-video"},
    {"slug": "proyectos", "nombre": "Proyectos de seguridad", "resumen": "Estudio y diseño a medida.", "detalle": "Estudio, evaluación y diseño de proyectos de seguridad y prevención de riesgos.", "img": "img/mision.jpg", "icono": "bi-clipboard-check"},
    {"slug": "instalaciones-industriales-mineras", "nombre": "Instalaciones Industriales y Mineras", "resumen": "Faenas de alta complejidad.", "detalle": "Protección para faenas mineras e industriales, prevención de riesgos y control de pérdidas operacionales.", "img": "img/instalaciones.jpg", "icono": "bi-buildings"},
]


class ServicioListaView(TemplateView):
    template_name = "servicios/lista.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["servicios"] = SERVICIOS
        return ctx


class ServicioDetalleView(TemplateView):
    template_name = "servicios/detalle.html"

    def get_context_data(self, slug, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            ctx["s"] = next(x for x in SERVICIOS if x["slug"] == slug)
        except StopIteration:
            raise Http404("Servicio no existe")
        ctx["servicios"] = SERVICIOS
        return ctx


class InstalacionesView(TemplateView):
    template_name = "servicios/instalaciones.html"
