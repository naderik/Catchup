
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Customized User model
    """

    # Disable date_joined as we have created_at
    date_joined = None

    username_validator = RegexValidator(
        regex=r"^[\w.+-]+$",
        message="Enter a valid username. This value may contain only letters, numbers, and ./+/-/_ characters.",
    )

    username = models.CharField(
        _("username"),
        max_length=64,
        unique=True,
        db_index=True,
        blank=False,
        help_text=_(
            "Required. 64 characters or fewer. Letters, digits and ./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists.")},
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
        db_index=True,
        blank=False,
        error_messages={"unique": _("A user with that email already exists.")},
    )

    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="followings"
    )
