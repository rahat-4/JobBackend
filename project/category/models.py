from django.contrib.auth import get_user_model
from django.db import models

from autoslug import AutoSlugField

from common.models import BaseModelWithUID

User = get_user_model()

class Job(BaseModelWithUID):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from="title")
    description = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(null=True, blank=True)
    salary_range = models.CharField(max_length=255, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    responsibility = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    additional_requirements = models.TextField(null=True, blank=True)
    compensation = models.TextField(null=True, blank=True)

    # FK
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(
        "company.Organization", on_delete=models.CASCADE, related_name="jobs"
    )

    def __str__(self):
        return f"Title: {self.title} , Position: {self.position}"

