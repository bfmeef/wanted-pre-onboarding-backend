from rest_framework import generics
from .serilaizers import RegistrationSerializer

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    