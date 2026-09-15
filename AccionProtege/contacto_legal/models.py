from django.db import models


class SolicitudContacto(models.Model):
    # Repara ?page_id=39 que hoy muestra [wpcf] roto.
    # Trazabilidad: P2-HU-03 -> P2-CU-02 -> RF-02
    # RUT/email = dato personal Ley 21.719: se guarda consentimiento + IP + fecha.
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    mensaje = models.TextField()
    acepta_privacidad = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"
