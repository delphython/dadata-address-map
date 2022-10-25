from django.db import models

# Create your models here.

class Addresses(models.Model):
    address = models.CharField(
        'Адрес',
        max_length=250,
        blank=True,
    )
    postal_code = models.CharField(
        'Индекс',
        max_length=6,
        blank=True,
    )

    country = models.CharField(
        'Страна',
        max_length=50,
        blank=True,
    )

    federal_district = models.CharField(
        'Федеральный округ',
        max_length=50,
        blank=True,
    )

    region_type = models.CharField(
        'Тип региона',
        max_length=10,
        blank=True,
    )

    region = models.CharField(
        'Регион',
        max_length=100,
        blank=True,
    )

    area_type = models.CharField(
        'Тип местности',
        max_length=5,
        blank=True,
    )

    area = models.CharField(
        'Местность',
        max_length=100,
        blank=True,
    )

    city_type = models.CharField(
        'Тип города',
        max_length=10,
        blank=True,
    )

    city = models.CharField(
        'Город',
        max_length=100,
        blank=True,
    )

    settlement_type = models.CharField(
        'Тип поселка',
        max_length=10,
        blank=True,
    )

    settlement = models.CharField(
        'Поселок',
        max_length=100,
        blank=True,
    )

    kladr_id = models.BigIntegerField(
        'Идентификатор в системе КЛАДР',
    )

    fias_id = models.CharField(
        'Идентификатор в системе ФИАС',
        max_length=36,
        blank=True,
    )

    fias_level = models.IntegerField(
        'Уровень в системе ФИАС',
    )

    capital_marker = models.IntegerField(
        'Метка столицы',
    )

    okato = models.CharField(
        'ОКАТО',
        max_length=11,
        blank=True,
    )

    oktmo = models.CharField(
        'ОКТМО',
        max_length=11,
        blank=True,
    )

    tax_office = models.CharField(
        'Номер налоговой',
        max_length=10,
        blank=True,
    )

    timezone = models.CharField(
        'Часовой пояс',
        max_length=6,
        blank=True,
    )

    geo_lat = models.DecimalField(
        'Широта',
        max_digits=9,
        decimal_places=6,
        db_index=True,
    )

    geo_lon = models.DecimalField(
        'Долгота',
        max_digits=9,
        decimal_places=6,
        db_index=True,
    )

    population = models.CharField(
        'Население',
        max_length=10,
        blank=True,
    )

    foundation_year = models.CharField(
        'Год основания',
        max_length=20,
        blank=True,
    )

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address
