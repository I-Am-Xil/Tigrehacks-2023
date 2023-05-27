from django.db import models

# Create your models here.
class Suscripcion:
    uuid = models.UUIDField(models.Model)
    fecha_ultimo_pago = models.DateField()
    vencimiento_suscripcio = models.DateField()
    estado_suscripcion = models.BooleanField()
     