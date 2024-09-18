from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Offer


# Los serializadores son clases que permiten convertir instancias de modelos en JSON.
# Serializador para el modelo Offer
class OfferSerializer(serializers.ModelSerializer):
    # Campo de solo lectura para mostrar el nombre de usuario del autor
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:  # Clase Meta para definir el modelo y los campos a serializar
        model = Offer
        fields = ['id', 'address', 'size', 'type', 'price', 'sharing', 'text', 'author']


# Serializador para el modelo User
class UserSerializer(serializers.ModelSerializer):
    # Campo para mostrar las ofertas del usuario
    offers = serializers.PrimaryKeyRelatedField(many=True, queryset=Offer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'offers']
