from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # automatically populates on create
    updated_at = models.DateTimeField(auto_now=True) # automatically set when saved, object.save()

    class Meta:
        abstract = True