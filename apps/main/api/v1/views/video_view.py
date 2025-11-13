from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.main.models import Video

from ..serializers import VideoSerializer


class VideoListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.all()
        content_type = self.request.query_params.get('content_type')
        if content_type:
            queryset = queryset.filter(content_type=content_type)
        return queryset
