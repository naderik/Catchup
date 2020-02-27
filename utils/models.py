import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Model(models.Model):
    """
    Base model
    """

    class Meta:
        abstract = True

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self.pk}>"