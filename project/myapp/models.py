import uuid

from django.db import models

from model_version import ModelVersion


class UUIDBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class MyModel(UUIDBaseModel, ModelVersion):
    name = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.name}"
