from django.db import models

from common.models import BaseModelWithUID


class Organization(BaseModelWithUID):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, populate_from="name")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
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