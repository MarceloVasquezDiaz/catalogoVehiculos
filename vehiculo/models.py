from django.db import models

# Create your models here.
marcas = (('Fiar', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota'))
categorias = (('particular', 'particular'), ('transporte', 'transporte'), ('carga', 'carga'))

class Vehiculo(models.Model):
    '''
    Modelo que representa un vehiculo.
    '''
    marca = models.CharField(max_length=20, default='Ford', choices=marcas)
    modelo = models.CharField(max_length=100)
    carroceria = models.CharField(max_length=50)
    motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, default='Particula', verbose_name='Categoría', help_text='Puede ser Particular, Transporte o Carga', choices=categorias)
    precio = models.IntegerField()
    fecha_de_creacion = models.DateField(auto_now_add=True, null=True, blank=True)
    fecha_de_modificacion = models.DateField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.marca} {self.modelo} {self.carroceria}'
    
    class Meta:
        permissions = [
            ('visualizar_catalogo', "Puede ver el catalogo de vehiculos")
        ]
