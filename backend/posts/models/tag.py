from django.db import models

from common.models.uuid_abstract_model import UUIDAbstractModel


class Tag(UUIDAbstractModel):
    name = models.CharField(max_length=100, unique=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
