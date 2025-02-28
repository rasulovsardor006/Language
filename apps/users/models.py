from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Profile(models.Model):
    phone = PhoneNumberField(_('Phone'))

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
