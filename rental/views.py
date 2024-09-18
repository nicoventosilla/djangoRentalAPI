from rest_framework import generics, permissions  # Importar las clases generics y permissions de rest_framework
from rental.models import Offer  # Importar el modelo Offer
from rental.serializers import OfferSerializer, \
    UserSerializer  # Importar los serializadores OfferSerializer y UserSerializer
from django.contrib.auth.models import User  # Importar el modelo User
from rental.permissions import IsAuthorOrReadOnly  # Importar la clase IsAuthorOrReadOnly


# Vista basada en clase para la lista de ofertas
class OfferList(generics.ListCreateAPIView):
    queryset = Offer.objects.all()  # Consultar todas las ofertas
    serializer_class = OfferSerializer  # Usar el serializador OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Permitir solo lectura a usuarios no autenticados

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Vista basada en clase para los detalles de una oferta
class OfferDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly  # Permitir solo lectura a usuarios no autenticados y solo escritura al autor
    ]


# Vista basada en clase para la lista de usuarios
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Vista basada en clase para los detalles de un usuario
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
