from django.db import models
from uuid import uuid4

# Create your models here.
class Suscripcion(models.Model):
    uuid = models.CharField(primary_key=True, max_length=36, default=uuid4)
    user_id = models.PositiveIntegerField()
    fecha_ultimo_pago = models.DateField(blank=True, null=True)
    vencimiento_suscripcion = models.DateField(blank=True, null=True)
    estado_suscripcion = models.BooleanField()

    class Meta:
        #managed = False
        db_table = 'suscripcion'