from rest_framework import serializers

from apps.main import models


class RegistrationSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = models.Registration
        fields = [
            'registration_type',
            'name',
            'email',
            'phone',
            'additional_info',
            'company_address',
            'contact_person'
        ]

class ReviewSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = models.Review
        fields = [
            'rating',
            'author',
            'author_position',
            'description'
        ]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = [
            'id',
            'content_type',
            'url',
            'title',
            'description',
        ]


class HistoryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoryPhoto
        fields = ['alt', 'photo']

class HistorySerializer(serializers.ModelSerializer):
    photo = HistoryPhotoSerializer(read_only=True)

    class Meta:
        model = models.History
        fields = [
            'id',
            'name',
            'description',
            'period',
            'city',
            'members',
            'trees',
            'photo',
        ]
