from django.db import models

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModelWithUID


class Organization(BaseModelWithUID):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=255, unique=True, populate_from="name")
    email = models.EmailField(blank=True, null=True)
    phone = PhoneNumberField(blank=True)
    description = models.TextField(blank=True, null=True)

    # Links
    website_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Uid: {self.uid} Name: {self.name}"