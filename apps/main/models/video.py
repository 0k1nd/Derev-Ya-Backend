from django.db import models

from apps.main import models as main_models


class Video(main_models.TimestampedModel):
    CONTENT_TYPE_CHOICES = [
        ('drone', 'Кадры с дрона'),
        ('report', 'Репортажи'),
    ]

    content_type = models.CharField(
        max_length=20,
        default='drone',
        choices=CONTENT_TYPE_CHOICES,
        verbose_name="Тип контента"
    )
    url = models.CharField(
        max_length=255,
        verbose_name="ссылка на видео"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="ссылка на видео"
    )
    description = models.TextField(verbose_name="Описание")

    class Meta(main_models.TimestampedModel.Meta):
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return f"{self.id}) {self.content_type}"
