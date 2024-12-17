from django.db import models
import uuid

# Create your models here.


class Autotimestamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )

    class Meta:
        abstract = True


class BaseModel(Autotimestamps, UUIDModel):
    class Meta:
        abstract = True
