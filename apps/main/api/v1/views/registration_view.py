from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.main.models import Registration

from ..serializers import RegistrationSerializer


class RegistrationCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
