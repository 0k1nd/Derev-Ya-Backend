from django.db import models


class Registration(models.Model):
    PERSON = 'person'
    COMPANY = 'company'
    REGISTRATION_TYPE_CHOICES = [
        (PERSON, 'Физическое лицо'),
        (COMPANY, 'ООО'),
    ]

    registration_type = models.CharField(
        max_length=20,
        choices=REGISTRATION_TYPE_CHOICES,
        default=PERSON,
        verbose_name="Тип регистрации"
    )

    name = models.CharField(max_length=255, verbose_name="ФИО / Название компании")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=30, verbose_name="Номер телефона")
    additional_info = models.TextField(
        blank=True,
        null=True,
        verbose_name="Дополнительная информация"
    )

    company_address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Адрес компании"
    )
    contact_person = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Контактное лицо"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрации"

    def __str__(self):
        return self.name
