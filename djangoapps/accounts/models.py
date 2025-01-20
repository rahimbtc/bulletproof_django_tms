from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator


class UserModel(AbstractUser):
    # Override the email field to make it unique and mandatory
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        validators=[EmailValidator],
        error_messages={
            "unique": "A user with this email already exists.",
        },
    )
    # extra fields
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = "user"
        ordering = ["-id"]
