from django.db import models

from apps.main.models import TimestampedModel


class City(TimestampedModel):
    name = models.CharField(
        max_length=25,
        verbose_name="Название города"
    )
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("-name",)

    def __str__(self):
        return self.name
