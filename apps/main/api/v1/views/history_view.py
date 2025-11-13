from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.main.models import History

from ..serializers import HistorySerializer


class HistoryListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = History.objects.all()
    serializer_class = HistorySerializer
