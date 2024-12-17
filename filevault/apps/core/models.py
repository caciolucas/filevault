import hashlib
import magic
from django.db import models
from private_storage.fields import PrivateFileField
from django.conf import settings
from django.utils import timezone

from common.models import BaseModel


class Client(BaseModel):
    name = models.CharField(max_length=255)
    client_id = models.CharField(max_length=50, unique=True)
    client_secret = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


def get_file_path(instance, filename: str):
    ext = filename.split(".")[-1]

    date = timezone.now()
    name = hashlib.sha256((settings.SECRET_KEY + str(date)).encode()).hexdigest()
    date = str(date)[0:19].replace(" ", "/").replace("-", "/").replace(":", "")

    client = instance.client.client_id
    return f"{client}/{date}/{name}.{ext}"


class File(BaseModel):
    client = models.ForeignKey("Client", on_delete=models.DO_NOTHING)
    name = models.CharField("Name", max_length=255)
    mime_type = models.CharField("Mime_type", max_length=255)
    size = models.BigIntegerField("Size")
    path = PrivateFileField("Path", upload_to=get_file_path)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.size = self.path.size
        super().save(*args, **kwargs)
        self.mime_type = magic.from_file(self.path.path, mime=True)
        super().save(*args, **kwargs)
