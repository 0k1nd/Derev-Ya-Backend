from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.main.models import TimestampedModel


class Review(TimestampedModel):
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        verbose_name="Рейтинг",
        default=3
    )
    author = models.CharField(
        verbose_name="Автор",
        max_length=255,
    )
    author_position = models.CharField(
        verbose_name="Должность автора",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="Текст комментария"
    )

    class Meta(TimestampedModel.Meta):
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.id}) {self.author}"
