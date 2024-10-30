from django.db import models

# Create your models here.
class Detalles(models.Model):
    ID_Detalles=models.IntegerField(primary_key=True)
    ID_Orden=models.IntegerField()
    ID_Cliente=models.IntegerField()
    Cantidad=models.IntegerField()
    Precio_Unitario=models.FloatField()
    Subtotal=models.FloatField()
    Descuento=models.FloatField()
    
    def __str__(self) -> str:
        return str(self.ID_Detalles)