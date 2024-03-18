from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from common.models import BaseModelWithUID

from .choices import AddressStatus
from .managers import AddressQuerySet

User = get_user_model()


class Division(BaseModelWithUID):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=20, decimal_places=15, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=20, decimal_places=15, null=True, blank=True
    )

    def __str__(self):
        return self.name


class District(BaseModelWithUID):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=20, decimal_places=15, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=20, decimal_places=15, null=True, blank=True
    )
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Upazila(BaseModelWithUID):
    """
    this is also police station
    """
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "district", "division")


class Address(BaseModelWithUID):
    label = models.CharField(max_length=255, blank=True)
    house_street = models.CharField(
        verbose_name="House and street", max_length=255, blank=True
    )
    upazila = models.ForeignKey(
        Upazila, on_delete=models.SET_NULL, null=True, blank=True
    )
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True, blank=True
    )
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True, blank=True
    )
    country = models.CharField(
        verbose_name="Country name", max_length=255, blank=True, default="Bangladesh"
    )
    status = models.CharField(
        max_length=20,
        choices=AddressStatus.choices,
        db_index=True,
        default=AddressStatus.ACTIVE,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.ForeignKey(
        "company.Organization", on_delete=models.SET_NULL, null=True, blank=True
    )
    objects = AddressQuerySet.as_manager()

    def __str__(self):
        return f"Division: {self.division}"

    def clean(self):
        if not self.user and not self.organization:
            raise ValidationError("Either 'user' or 'organization' must be set.")

