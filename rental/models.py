from django.db import models

# Opciones para el tamaño de la propiedad
SIZE_CHOICES = [
    ('ST', 'Studio'),
    ('1BR', '1 bedroom'),
    ('2BR', '2 bedrooms'),
    ('3BR', '3 bedrooms'),
    ('MBR', '3+ bedrooms'),
]

# Opciones para el tipo de propiedad
TYPE_CHOICES = [
    ('H', 'house'),
    ('APT', 'apartment'),
]


# Modelo de datos para una oferta de alquiler
class Offer(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    address = models.CharField(max_length=100, blank=True, default='')  # Dirección
    size = models.CharField(choices=SIZE_CHOICES, default='1BR', max_length=100)  # Tamaño
    type = models.CharField(choices=TYPE_CHOICES, default='APT', max_length=100)  # Tipo
    price = models.PositiveIntegerField(default=0)  # Precio
    sharing = models.BooleanField(default=False)  # Compartido
    text = models.TextField(default='')  # Descripción
    author = models.ForeignKey('auth.User', related_name='offers', on_delete=models.CASCADE)  # Autor

    class Meta:
        ordering = ['created']  # Ordenar por fecha de creación
