from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


# Create your models here.


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Body"))
    image = models.ImageField(_("Image"), null=True, blank=True)
    resized_image = ResizedImageField(size=[500, 300], upload_to='whatever', crop=['middle', 'center'],
                                      force_format='PNG', null=True, blank=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title
