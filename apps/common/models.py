from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

class Country(models.Model):
    name = models.CharField(_('Name'), max_length=155)
    ico_code =  models.CharField(_('Ico Code'), max_length=128, unique=True)
    icon  = models.ImageField(_('Icon'), upload_to="country/")


    class Meta:
        verbose_name =  _("Country")
        verbose_name_plural = _("Countries")


    def __str__(self):
        return self.name
    



class MainConfiguration(SingletonModel):
    app_store_url = models.CharField(_("Application Store"), max_length=128)
    play_market_url = models.CharField(_("Play Market"), max_length=128)

    class Meta:
        verbose_name = _("Main configuration")
        verbose_name_plural = _("Main configuration")

    def __str__(self):
        return f'{self.app_store_url} | {self.play_market_url}'
