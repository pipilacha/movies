from django.db import models

from moviesapp.models import BaseModel


class Actor(BaseModel):
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
