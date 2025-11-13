from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.main.models import Review

from ..serializers import ReviewSerializer


class ReviewListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
