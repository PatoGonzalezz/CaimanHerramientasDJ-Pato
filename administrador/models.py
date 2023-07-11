from django.db import models

# Create your models here.
class Tipo(models.Model):
    id_tipo     = models.AutoField(db_column='idTipo', primary_key=True)
    tipo        = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipo)

class Producto(models.Model):
    id_producto     = models.CharField  (primary_key = True, max_length= 10)
    foto_producto   = models.ImageField (null = True, blank = True)
    nombre          = models.CharField  (max_length=100)
    marca           = models.CharField  (max_length=100)
    id_tipo         = models.ForeignKey ('Tipo',on_delete=models.CASCADE, db_column='idTipo') 
    precio          = models.IntegerField ()
    stock           = models.CharField  (max_length=100)
    
    def __str__(self):
        return str(self.id_producto)+" "+str(self.nombre)+" "+str(self.marca)