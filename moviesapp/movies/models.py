from django.db import models

from moviesapp.models import BaseModel
from actors.models import Actor
from genders.models import Genders

import uuid


class Movies(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False)
    genders = models.ManyToManyField(Genders)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    description = models.CharField(max_length=300, blank=False)
    release_date = models.DateTimeField(blank=False)
    actors = models.ManyToManyField(Actor)
    image = models.URLField(blank=False)
    availability = models.CharField(default='Available')
