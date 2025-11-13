from django.db import models

from apps.main import models as main_models


class History(main_models.TimestampedModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(verbose_name="Описание")
    period = models.CharField(
        max_length=255,
        verbose_name="Период проведения работ",
        help_text="формат 'Апрель 15-16,2024'"
        )
    city = models.ForeignKey(
        main_models.City,
        on_delete=models.CASCADE,
        verbose_name="Город проведения"
    )
    members = models.PositiveIntegerField(
        default=1,
        verbose_name="Количество участников"
    )
    trees = models.PositiveIntegerField(
        default=1,
        verbose_name="Количество деревьев"
    )

    class Meta(main_models.TimestampedModel.Meta):
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"



class HistoryPhoto(models.Model):
    history = models.OneToOneField(
        History,
        on_delete=models.CASCADE,
        verbose_name="Карточка истории",
        related_name='photo'
        )
    alt = models.CharField("Alt-текст", max_length=255)
    photo = models.ImageField("Фотография", upload_to="history/photos/")


    class Meta:
        verbose_name = "Фотография для карточки"
        verbose_name_plural = "Фотографии для карточек"
